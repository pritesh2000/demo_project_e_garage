# from django.contrib import admin
from django.urls import include, path
from .views import OwnerList

urlpatterns = [
    path('', OwnerList.as_view())    
]
