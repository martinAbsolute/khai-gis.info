from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.utils.translation import LANGUAGE_SESSION_KEY

# Create your views here.

def blogmain(request):
    request.session[LANGUAGE_SESSION_KEY] = 'uk'
    post_list = list(reversed(Posts.objects.all()))
    post_list_en = list(reversed(Posts.objects.all().filter(en=True)))
    post_list_ru = list(reversed(Posts.objects.all().filter(ru=True)))
    paginator = Paginator(post_list, 5)
    paginator_en = Paginator(post_list_en, 5)
    paginator_ru = Paginator(post_list_ru, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    posts_en = paginator_en.get_page(page)
    posts_ru = paginator_ru.get_page(page)
    context = {
        'posts' : posts,
        'posts_en' : posts_en,
        'posts_ru' : posts_ru,
        'active' : 'blog',
        'paginator' : paginator,
        'paginator_en' : paginator_en,
        'paginator_ru' : paginator_ru,
    }
    return render(request, 'blog/blogmain.html', context)

def international(request):
    request.session[LANGUAGE_SESSION_KEY] = 'uk'
    post_list = list(reversed(Posts.objects.all().filter(category="МІЖНАРОДНІ ЗВ'ЯЗКИ")))
    post_list_en = list(reversed(Posts.objects.all().filter(category="МІЖНАРОДНІ ЗВ'ЯЗКИ").filter(en=True)))
    post_list_ru = list(reversed(Posts.objects.all().filter(category="МІЖНАРОДНІ ЗВ'ЯЗКИ").filter(ru=True)))
    paginator = Paginator(post_list, 1)
    paginator_en = Paginator(post_list_en, 1)
    paginator_ru = Paginator(post_list_ru, 1)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    posts_ru = paginator_en.get_page(page)
    posts_en = paginator_ru.get_page(page)
    context = {
        'posts' : posts,
        'posts_en' : posts_en,
        'posts_ru' : posts_ru,
        'active' : 'international',
        'paginator' : paginator,
        'paginator_en' : paginator_en,
        'paginator_ru' : paginator_ru,
    }
    return render(request, 'blog/blogmain.html', context)

def blogpost(request, slug):
    request.session[LANGUAGE_SESSION_KEY] = 'uk'
    post = get_object_or_404(Posts, slug=slug)
    context = {
        'post' : post,
        'active' : 'blog',
    }
    return render(request, 'blog/blogpost.html', context)