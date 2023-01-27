from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField(max_length=15)
    email = models.EmailField(max_length=25)
    message =models.TextField(max_length=500)