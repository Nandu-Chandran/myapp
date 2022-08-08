from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog_home'),
    path('about/', views.about, name='blog-about'),
    path('<str:msg>', views.viewfile, name = 'blog-about'),
]