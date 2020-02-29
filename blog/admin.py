from django.contrib import admin

# Register your models here.
from .models import Posts, PostImage, PostFile
from .models import GalleryImage, Gallery, GalleryCategory
from .models import MuseumImage, Museum

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1

class GalleryAdmin(admin.ModelAdmin):
    inlines = [ GalleryImageInline, ]

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1

class PostFileInline(admin.TabularInline):
    model = PostFile
    extra = 1

class PostsAdmin(admin.ModelAdmin):
    inlines = [ PostImageInline, PostFileInline, ]

class MuseumImageInline(admin.TabularInline):
    model = MuseumImage
    extra = 1

class MuseumAdmin(admin.ModelAdmin):
    inlines = [ MuseumImageInline, ]

admin.site.register(Posts, PostsAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryCategory)
admin.site.register(Museum, MuseumAdmin)