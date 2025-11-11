from django.db import models

# Create your models here. 
class Users(models.Model):
    name=models.CharField(max_length=50) 
    phone_number=models.CharField(max_length=50) 
    adress=models.CharField(max_length=50) 
    role=models.CharField(max_length=50) 
     
     
     