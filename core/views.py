from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
class UserLogin(LoginView):
    template_name = 'core/login.html'

class UserLogout(LogoutView):
    template_name = 'core/logout.html'
    # pass

