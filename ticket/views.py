# from multiprocessing import context
# from django.http import HttpResponse
# from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView 
from .models import Ticket

# Create your views here.
class CreateTicket(CreateView):
    model = Ticket
    fields = ['ticket_title', 'ticket_discription']
    template_name = 'ticket/create_ticket.html'
    success_url = '/ticket/view/'

class ViewTicket(TemplateView):             # template view is not taught yet.
    # model = Ticket    
    # punch = model.objects.all().values()
    template_name = 'ticket/ticket.html'
    # print(punch)
    # print('hello')
    # context_object_name = 'viewticket'

    # list1 = []
    # for j in range(len(punch)):
    #     for i in punch[j].values():
    #         list1.append(i)

    
    # print(list1)
