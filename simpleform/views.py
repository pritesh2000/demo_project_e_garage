from django.shortcuts import render

# Create your views here.
from .forms import AddressForm
from .models import Address
from django.views.generic.edit import CreateView


class CreateAddress(CreateView):
    form_class = AddressForm
    # model = Address
    template_name = 'address/address_form.html'
    success_url = '/ticket/view'
