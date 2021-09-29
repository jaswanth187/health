from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    name=models.CharField(max_length=20,blank=False)
    phone=models.CharField(max_length=12,blank=False)
    company_name=models.CharField(max_length=30,blank=False)
    
