from django.db import models

# Create your models here.

class Service(models.Model):
    service_name = models.CharField(max_length=50)
    service_price = models.IntegerField()
    service_discription = models.TextField()
    service_quantity = models.IntegerField()
    service_vehicle_num = models.CharField(max_length=50, null = True)
    service_status = models.BooleanField(default = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class ServiceCategory(models.Model):
# class ServiceCategory(Service):
    category_name = models.CharField(max_length=50)
    category_discription = models.TextField()
    class Meta:
        db_table = 'category'