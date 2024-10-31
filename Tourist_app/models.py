from django.db import models

# Create your models here.

class TouristApp(models.Model):
    Place_Name=models.CharField(max_length=200)
    Weather=models.CharField(max_length=200)
    State = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    Google_Map_Link=models.URLField(max_length=500)
    Image=models.ImageField(upload_to='tourist/')
    Description=models.CharField(max_length=2000)

class AdminRegister(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    conf_password=models.CharField(max_length=200)

class Login(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
