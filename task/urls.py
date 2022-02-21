

from django.urls import path
from .views import CreateTask, DeleteTask, TaskDetail,UpdateTask
from task import views


urlpatterns = [
    path('add/', CreateTask.as_view()),
    path('view/', views.index),
    path('<pk>/delete/', DeleteTask.as_view()),
    path('<pk>/update/', UpdateTask.as_view()),
    path('<pk>/view/', TaskDetail.as_view()),
    
]

