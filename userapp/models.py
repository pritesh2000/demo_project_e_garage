from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


"""There is Problem in models so userapp app is not complete."""


# Create your models here.
class Role(models.Model):
    role_id = models.AutoField(primary_key=True, unique=True)
    role_name = models.CharField(max_length=150, unique=True)

    class Meta():
        db_table = 'Role'


class User(AbstractUser):
    
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=130, unique= True)
    # print("first")
    first_name = models.CharField(max_length=150)
    # print("last")
    last_name = models.CharField(max_length=150)
    # print("password")
    password = models.CharField(max_length=150) 
    # print("email")
    email = models.EmailField(_('email') ,max_length=150, unique=True)
    
    phone_regex = RegexValidator(regex=r'^[6-9]{1}\d{9}', message='Phone number must be in the format : 9999999999')
    mobile_number = models.CharField(validators=[phone_regex], blank=True, unique=True ,max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta():
        db_table = 'User'

    def __str__(self):
        return self.username