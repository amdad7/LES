from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import CharField
#from django.db.models.enums import Choices
# Create your models here.

class Student(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    is_leader=models.BooleanField(default=False)
    phone_no=models.CharField(max_length=15,default=None)
    address=models.TextField(max_length=100,default=None)
    rollno=models.IntegerField(default=0)
    name=models.CharField(max_length=100)
    is_changed=models.BooleanField(default=False)
    choices=[
        ('C2','C2'),
        ('P5','P5')
    ]
    section=models.CharField(max_length=10,choices=choices)
    
    def __str__(self):
        return self.user.username



    @property
    def email(self):
        return self.user.email        


class Teacher(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    is_changed=models.BooleanField(default=True)
    def __str__(self):
        return self.user.username

    @property
    def name(self):
        return self.user.username
