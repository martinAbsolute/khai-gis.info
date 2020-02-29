"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from myapp import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]


urlpatterns += i18n_patterns (
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('abit/', views.abit, name='abit'),
    path('contact/', views.contact, name='contact'),
    path('tinymce/', include('tinymce.urls')),
    path('gallery/<slug:slug>/', views.gallery, name='gallery'),
    path('gallery/', views.gallery, name='gallery'),
    path('library/', views.library, name='library'),
    path('gisdayteaser/', views.gisdayteaser, name='gisdayteaser'),
    path('museum/', views.museum, name='museum'),
    path('museum/<slug:slug>/', views.museum, name='museum'),
    path('stud/', views.stud, name='stud'),
    path('internationalprojects/', views.maintenance, name='maintenance'),
    path('remotesensingdata/', views.maintenance, name='maintenance'),
    path('museum/', views.maintenance, name='maintenance'),
 )