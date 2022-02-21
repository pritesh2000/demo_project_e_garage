# from django.contrib import admin
from django.urls import path
from service import views

urlpatterns = [
    path('addservice/', views.addService),
    path('viewservice/', views.viewService),
    path('servicepage/', views.servicepage) 
]
