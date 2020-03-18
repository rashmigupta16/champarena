from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30 , null= True)
    last_name = models.CharField(max_length=30,null= True)
    mobile = models.CharField(max_length=12 , default = '1234')
    email = models.EmailField(max_length=254, default='', help_text='Required. Inform a valid email address.')


def __str__(self):
    return self.user
