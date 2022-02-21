from django import views
# from django.contrib import admin
from django.urls import path
from orm import views

urlpatterns = [
    path('studentdata/', views.studentData)
]
