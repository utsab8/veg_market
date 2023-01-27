from django.db import models

# Create your models here.
class Title(models.Model):
    title = models.CharField(max_length=500)

class Customers(models.Model):
    image = models.ImageField(upload_to="media/customers/")
    name = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)