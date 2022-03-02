from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.
class Secretary(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    pic=models.FileField(upload_to='profile',default='pofile.png')
    verify=models.BooleanField(default=False)

    def __str__(self):
        return self.name +'@'+self.email 




class House(models.Model):
    room_no = models.IntegerField(unique=True)
    image=models.FileField(upload_to='house-image',blank=True,null=True)

    def __int__(self):
        return self.room_no 





class Member(models.Model):
    doc_choice = (('pan','PAN Card '), ('aadhar','AAdhar Card'))

    house = models.ForeignKey(House,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    doc = models.CharField(max_length=20,choices=doc_choice)
    doc_number = models.CharField(max_length=15)
    address = models.TextField()
    verify = models.BooleanField(default=False)
    pic = models.FileField(upload_to='member_pic',default='member-pic.png') 


    def __str__(self):
        return self.name+'@'+self.name




class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    contact_no = models.IntegerField( )


    def __str__(self):
        return self.name +'@'+self.email
    




class Gallery(models.Model):
    name = models.CharField(max_length=30)
    image = models.FileField(upload_to='Gallery-image', null=True ,blank=True)


    def __str__(self):
        return self.name