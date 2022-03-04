from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee

# Create your views here.

def addEmployee(request):
    emp = Employee(ename = 'John',eage = 25, eemail = 'John@gmail.com', econtact = 1234567890)
    emp.save()
    return HttpResponse("Employee Added...")

def viewEmployee(request):
    employees = Employee.objects.all().values_list()    
    return render(request, 'employee/view.html', {'employees':employees})

def deleteEmployee(request):
    emp = Employee.objects.get(id=1)
    emp.delete()
    return HttpResponse("Employee delete...")

def updateEmployee(request):
    emp = Employee.objects.get(id=2)
    emp.eage = 30
    emp.econtact = 987654321
    emp.save()
    return HttpResponse("Employee updated...")
    