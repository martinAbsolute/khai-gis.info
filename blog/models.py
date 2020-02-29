from django.db import models
from datetime import datetime
from tinymce import HTMLField #TinyMce4-Lite
from django_thumbs.fields import ImageThumbsField # GENERATES THUMBNAILS, NEED TO INSTALL DJANGO_THUMBS!!
from django.db.models.signals import pre_save
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from unidecode import unidecode
from django.utils import timezone

import uuid
import os

# Create your models here.

def get_file_path_blog(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        now = timezone.now()
        return os.path.join('blogphotos/'+now.strftime('%Y')+'/'+now.strftime('%m')+'/'+now.strftime('%d'), filename)

class Posts(models.Model):
    title = models.CharField("Заголовок",max_length=400, help_text="Заголовок Новости")
    entitle = models.CharField("Английский Заголовок",max_length=400, help_text="Английский заголовок Новости", blank=True)
    rutitle = models.CharField("Русский Заголовок",max_length=400, help_text="Русский заголовок Новости", blank=True)
    en = models.BooleanField("Английская версия есть", help_text="Новость на английском", default=False)
    ru = models.BooleanField("Русская версия есть", help_text="Новость на русском", default=False)
    abstract = models.TextField("Аннотация", blank=True, help_text="Аннотация для баннера на главной")
    enabstract = models.TextField("Английская Аннотация", help_text="Английская аннотация для баннера на главной", blank=True)
    ruabstract = models.TextField("Русская Аннотация", help_text="Русская аннотация для баннера на главной", blank=True)
    body = HTMLField("Текст", help_text="Текст Новости")
    enbody = HTMLField("Английский Текст", help_text="Английский Текст Новости", blank=True)
    rubody = HTMLField("Русский Текст", help_text="Русский Текст Новости", blank=True)
    date = models.DateField("Дата", default=datetime.now, null=True, help_text="Дата Новости")
    NEWS_CATEGORY = (
    ("ПОДІЇ", "ПОДІЇ"),
    ("МІЖНАРОДНІ ЗВ'ЯЗКИ", "МІЖНАРОДНІ ЗВ'ЯЗКИ"),
    ("СТАТТІ", "СТАТТІ"),
    ("СТУДЕНТСЬКЕ ЖИТТЯ", "СТУДЕНТСЬКЕ ЖИТТЯ"),
    )
    category = models.CharField("Категория", max_length=19, choices=NEWS_CATEGORY, default="ПОДІЇ", help_text="Категория Новости")
    NEWSSIZES = (
        {'code': 'banner', 'wxh': '1024x576', 'resize': 'scale'},
    )
    newsfeed = ImageThumbsField("Баннер", upload_to=get_file_path_blog, help_text="Изображение для Новости на главной ! ДОЛЖНО БЫТЬ 16:9 !", sizes=NEWSSIZES)
    slug = models.SlugField(unique=True,editable=False,max_length=160) #Slug - генерирует уникальный url
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Новости"
        verbose_name = "Новость"
    def save(self, *args, **kwargs):
        now = timezone.now()
        self.slug = slugify(unidecode(self.title+now.strftime('%m')+now.strftime('%Y')+now.strftime('%d')))
        super(Posts, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return "/blog/%s/" % self.slug

class GalleryCategory(models.Model):
    name = models.CharField("Оглавление категории", max_length=255)
    class Meta:
        verbose_name = "Категория галереи"
        verbose_name_plural = "Категории галерей"
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return "/gallery/%s/" % Gallery.objects.filter(category=self).latest('id').slug

class Gallery(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создана")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлена")
    category = models.ForeignKey(GalleryCategory, verbose_name="Категория", null=True, blank=True, on_delete=models.CASCADE, related_name="gals")
    title = models.CharField("Название Галереи", max_length=255)
    slug = models.SlugField(unique=True,editable=False,max_length=160)
    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super(Gallery, self).save(*args, **kwargs)
    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return "/gallery/%s/" % self.slug

def get_file_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        now = timezone.now()
        return os.path.join('galleryphotos/'+now.strftime('%Y')+'/'+now.strftime('%m')+'/'+now.strftime('%d'), filename)
        
class GalleryImage(models.Model):
    SIZES = (
        {'code': 'thumb', 'wxh': '500x500', 'resize': 'crop'},
        {'code': 'bigthumb', 'wxh': '1000x1000', 'resize': 'crop'},
    )
    image = ImageThumbsField("Файл изображения", upload_to=get_file_path, help_text="Файл фотографии для галереи", sizes=SIZES)
    gallery = models.ForeignKey(Gallery, verbose_name="Галерея", related_name='images', on_delete=models.CASCADE)
    title = models.CharField("Оглавление фотографии", default="", max_length=255)
    description = models.TextField("Описание фотографии", default="")
    class Meta:
        verbose_name = "Фотография в галерее"
        verbose_name_plural = "Фотографии в галерее"
    def __str__(self):
        return self.title

class PostImage(models.Model):
    posts = models.ForeignKey(Posts, verbose_name="Посты" ,related_name='images', on_delete=models.CASCADE)
    SIZES = (
        {'code': 'thumb', 'wxh': '750x400', 'resize': 'crop'},
    )
    image = ImageThumbsField("Изображение", sizes=SIZES, upload_to=get_file_path_blog)
    description = models.CharField("Описание изображения", max_length=300, blank=True, default="")

class PostFile(models.Model):
    posts = models.ForeignKey(Posts, verbose_name="Посты" ,related_name='files', on_delete=models.CASCADE)
    filename = models.FileField("Прикрепленный Файл", null=True, blank=True, upload_to=get_file_path_blog)
    description = models.CharField("Описание Файла", max_length=300, blank=False)

class Museum(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлён")
    title = models.CharField("Название Музея", max_length=255)
    slug = models.SlugField(unique=True,editable=False,max_length=160)
    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super(Museum, self).save(*args, **kwargs)
    class Meta:
        verbose_name = "Музей"
        verbose_name_plural = "Музеи"
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return "/museum/%s/" % self.slug
    def get_file_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        now = timezone.now()
        return os.path.join('museumphotos/'+now.strftime('%Y')+'/'+now.strftime('%m')+'/'+now.strftime('%d'), filename)
        
class MuseumImage(models.Model):
    SIZES = (
        {'code': 'thumb', 'wxh': '500x500', 'resize': 'crop'},
        {'code': 'bigthumb', 'wxh': '1000x1000', 'resize': 'crop'},
    )
    DEFAULT_EXAM_ID = 1
    image = ImageThumbsField("Файл фотографии экспоната", upload_to=get_file_path, help_text="Файл фотографии экспоната", sizes=SIZES)
    museum = models.ForeignKey(Museum, default=DEFAULT_EXAM_ID, verbose_name="Музей", related_name='images', on_delete=models.CASCADE)
    title = models.CharField("Оглавление экспоната", default="", max_length=255)
    description = models.TextField("Описание экспоната", default="")
    class Meta:
        verbose_name = "Экспонат в музее"
        verbose_name_plural = "Экспонаты в музее"
    def __str__(self):
        return self.title