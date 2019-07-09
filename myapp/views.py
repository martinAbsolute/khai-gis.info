from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from blog.models import Posts, Gallery, GalleryCategory

# Create your views here.

def index(request):
    posts = list(reversed(Posts.objects.all()))[:6]
    posts_en = list(reversed(Posts.objects.all().filter(en=True)))[:6]
    posts_ru = list(reversed(Posts.objects.all().filter(ru=True)))[:6]
    context = {
        'posts' : posts,
        'posts_en' : posts_en,
        'posts_ru' : posts_ru,
        'active' : 'index',
    }
    return render(request, 'mainpage/index.html', context)

def abit(request):
    context = {
        'active' : 'abit',
    }
    return render(request, 'mainpage/abit.html', context)

def stud(request):
    context = {
        'active' : 'stud',
    }
    return render(request, 'mainpage/stud.html', context)

def gisdayteaser(request):
    context = {
        'active' : 'gisdayteaser',
        'HideHeader' : True,
    }
    return render(request, 'mainpage/gisdayteaser.html', context)

def contact(request):
    context = {
        'active' : 'contact',
    }
    return render(request, 'mainpage/contact.html', context)

def gallery(request, slug=""):
    if slug == "":
        slug = Gallery.objects.latest('id').slug
    gallery = get_object_or_404(Gallery, slug=slug)
    category = Gallery.category
    categories = GalleryCategory.objects.all()
    context = {
        'categories' : categories,
        'category' : category,
        'gallery' : gallery,
        'active' : 'gallery',
    }
    return render(request, 'mainpage/gallery.html', context)

def library(request):
    context = {
        'active' : 'library',
    }
    return render(request, 'mainpage/library.html', context)

def maintenance(request):
    context = {
        'active' : 'maintenance',
    }
    return render(request, 'mainpage/maintenance.html', context)