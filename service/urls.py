from django.contrib import admin
from django.urls import include, path
from service import views

urlpatterns = [
    path('addservice/', views.addService),
    path('viewservice/', views.viewService),
    path('servicepage/', views.servicepage) 
]
