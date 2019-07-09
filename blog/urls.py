from django.urls import path
from blog import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('international/', views.international, name='international'),
    path('<slug:slug>/', views.blogpost, name='blogpost'),
    path('', views.blogmain, name='blogmain'),
]