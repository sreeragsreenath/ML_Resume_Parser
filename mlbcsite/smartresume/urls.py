from django.contrib.auth import authenticate, login ,logout
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('upload_file', views.upload_file, name='upload_file'),
    path('userLogin', views.userLogin, name='userLogin'),
    path('register' , views.register, name='register'),
    path('logout_view' , views.logout_view, name='logout_view')
]