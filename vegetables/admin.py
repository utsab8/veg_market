from django.contrib import admin
from .models import VegList, VegTitle

# Register your models here.


admin.site.register(VegTitle)

admin.site.register(VegList)