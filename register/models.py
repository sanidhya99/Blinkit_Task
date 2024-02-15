from django.db import models
from django.contrib.auth.models import AbstractUser
from .manage import *
class CustomUser(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    name=models.CharField(max_length=20)
    number=models.CharField(max_length=12)
    objects=UserManager()
    
    REQUIRED_FIELDS=[]

    USERNAME_FIELD='email'


