from django.db import models

# Create your models here.
class Owner(models.Model):
    owner_name = models.CharField(max_length=50)
    owner_email = models.EmailField(max_length=50)
    owner_contact = models.IntegerField()
    owner_address = models.TextField()

    class Meta:
        db_table = 'owner'
