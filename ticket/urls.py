# from django.contrib import admin
from django.urls import include, path

from .views import CreateTicket,ViewTicket

urlpatterns = [

    path('add/', CreateTicket.as_view()),
    path('view/', ViewTicket.as_view())

]