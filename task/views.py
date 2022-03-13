from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Task
from django.views.generic import DetailView

# Create your views here.
class CreateTask(CreateView):
    model = Task
    fields = ['task_name', 'task_discription']
    template_name = 'task/create_task.html'
    success_url = '/task/view'

class DeleteTask(DeleteView):
    model = Task
    success_url = '/task/view'

def index(request):        
    return render(request, 'task/index.html')

class UpdateTask(UpdateView):
    model = Task 
    fields = ['task_name', 'task_discription']
    template_name = 'task/update_task.html'
    success_url = '/task/view'

class TaskDetail(DetailView):
    model = Task
    template_name = 'task/task_detail.html'