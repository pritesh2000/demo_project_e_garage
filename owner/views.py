from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Owner

# Create your views here.

class OwnerList(ListView):
    model = Owner
    ownerlist = model.objects.all()
    template_name = 'owner/owner_list.html'
    context_object_name = 'ownerlist'

    def addWork(request):
        return HttpResponse("Work added...")        
