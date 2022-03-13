from django.urls import path
from .views import BaseRegisterView, UserLoginView
from userapp import views


urlpatterns = [
    path('user-registration/', BaseRegisterView.as_view(), name = 'user_registration'),
    path('user-login/', UserLoginView.as_view(), name = 'user_login'),
    path('index/', views.index)
]

