from django.db import models

# Create your models here.





class VegTitle(models.Model):
	name = models.CharField(max_length = 200)
	
	content = models.TextField()
 
 
class VegList(models.Model):
    image = models.ImageField(upload_to= "media/vegetable/")
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    
    

    