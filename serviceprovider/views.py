from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import ServiceProvider

# Create your views here.
class AddServiceProvider(CreateView):
    model = ServiceProvider
    fields = ['name', 'address', 'email', 'phone', 'website', 'description']
    template_name = 'serviceprovider/add_serviceprovider.html'
    success_url = '/serviceprovider/view'

class ViewServiceProvider(ListView):
    model = ServiceProvider
    serviceproviders = model.objects.all()
    context_object_name = 'serviceproviders'
    template_name = 'serviceprovider/view_serviceprovider.html'

class DetailServiceProvider(DetailView):
    model = ServiceProvider
    template_name = 'serviceprovider/detail_serviceprovider.html'
    context_object_name = 'serviceprovider'

class DeleteServiceProvider(DeleteView):
    model = ServiceProvider
    template_name = 'serviceprovider/delete.html'
    success_url = '/serviceprovider/view'

class UpdateServiceProvider(UpdateView):
    model = ServiceProvider
    fields = ['name', 'address', 'email', 'phone', 'website', 'description']
    template_name = 'serviceprovider/update_serviceprovider.html'
    success_url = '/serviceprovider/view'

