from django.db import models

# Create your models here.
class HomeImage(models.Model):
    image = models.ImageField(upload_to="media/home/")

class HomeContent(models.Model):
    count = models.IntegerField(max_length=200)
    title = models.CharField(max_length=200)
    
    button = models.CharField(max_length=200)