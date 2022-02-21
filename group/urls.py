# from django.contrib import admin
from django.urls import path
from group import views

urlpatterns = [
    path('add/', views.group),
    path('contactUs/', views.contactUs),
    path('', views.index),
    path('aboutUs/', views.aboutUs)
]
