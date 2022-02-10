from django.http import HttpResponse
from django.shortcuts import render

# Create your views here. 
# for group

def group(request):
    return HttpResponse("Group is called...")

def contactUs(request):
    return render(request, 'group/contactUs.html')

def index(request):
    return render(request, 'group/index.html')

def aboutUs(request):
    return render(request, 'group/aboutUs.html')