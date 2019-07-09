from django.contrib import admin

# Register your models here.
from .models import Posts, PostImage, PostFile
from .models import GalleryImage, Gallery, GalleryCategory

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

admin.site.register(Posts, PostsAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryCategory)