from django.http import HttpResponse
from django.shortcuts import render

# Create your views here. 
# for group

def group(request):
    return HttpResponse("Group is called...")

def contactUs(request):
    context = {
        'contact_name' : ["Pritesh", "Sharad", "Ashish", "Yash", "Anil"]
    }
    return render(request, 'group/contactUs.html', context)

def index(request):
    context = {
        'name' : 'E-GARAGE'
    }
    return render(request, 'group/index.html', context)

def aboutUs(request):
    context = {
        'isActive' : True,
        'age' : 20
    }
    return render(request, 'group/aboutUs.html', context)
    