from django.db import models

# Create your models here.
class Address(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)

    class Meta():
        db_table = 'address'
