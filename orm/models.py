from sre_constants import CATEGORY
from telnetlib import STATUS
from django.db import models

# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=50)
    role_description = models.TextField()
    class Meta:
        db_table = 'role'

class Employee(Role):
    employee_name = models.CharField(max_length=50)
    employee_email = models.CharField(max_length=50)
    employee_password = models.CharField(max_length=50)
    employee_phone = models.CharField(max_length=50)
    employee_address = models.TextField()
    employee_dob = models.DateField()
    
    class Meta:
        db_table = 'employee'

class Student(models.Model):
    # role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    role_id = models.OneToOneField(Role, on_delete=models.CASCADE)      # for one to one
    student_name = models.CharField(max_length=50)
    student_email = models.CharField(max_length=50)
    student_password = models.CharField(max_length=50)
    student_phone = models.CharField(max_length=50)
    student_address = models.TextField()
    student_dob = models.DateField()

    class Meta:
        db_table = 'student'    


class Customer(models.Model):
    customer_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'customer'

class Product(models.Model):
    CATEGORY = (('inner', 'inner'), ('outer','outer'))
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    data_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'product'

class Order(models.Model):
    STATUS = (
        ('pending', 'pending'),('processing', 'processing'), ('completed', 'completed')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    STATUS = models.CharField(max_length=200, choices=STATUS)


    class Meta:
        db_table = 'order'
