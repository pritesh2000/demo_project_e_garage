from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# create add service function to add new service to app
def addService(request):
    print("Add service calling")
    return HttpResponse("Add pservice called")

# create view service function to view about provided service
def viewService(request):
    return HttpResponse("View service called...")

# create service page function to get to web page
def servicepage(request):
    return render(request, 'service/servicepage.html')