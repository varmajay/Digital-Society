from operator import mod
from django.db import models

# Create your models here.
class Secretary(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    pic=models.FileField(upload_to='profile',default='pic.png',null=True,blank=True)
    verify=models.BooleanField(default=False)

    def __str__(self):
        return self.name +'@'+self.email 
        