from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='users_home'),
    path('about/', views.about, name='users-about'),
]