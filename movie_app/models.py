from tkinter import CASCADE
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    duration = models. CharField(max_length=20)
    poster = models.FileField(upload_to='upload/videos')
    categories = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Signup(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=30)
  
    
    def __str__(self):
        return self.username
    
class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
   
    
    def __str__(self):
        return self.username
    

