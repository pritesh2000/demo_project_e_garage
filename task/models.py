from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_discription = models.TextField()

    class Meta():
        db_table = 'task'