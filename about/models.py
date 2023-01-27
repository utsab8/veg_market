from django.db import models

# Create your models here.

class About(models.Model):
    image = models.ImageField(upload_to="media/about/")
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    button = models.CharField(max_length=100)
    