from django.db import models

# Create your models here.

class Products(models.Model): 
    barcode = models.CharField(max_length=32, blank=True, default='') 
    name = models.CharField(max_length=128, blank=True, default='') 
    ingridients = models.CharField(max_length=1024, blank=True, default='') 
    status = models.CharField(max_length=16, blank=True, default='') 
    why_haram = models.CharField(max_length=1024, blank=True, default='')  
    why_doubtful = models.CharField(max_length=1024, blank=True, default='') 

    class Meta: 
        ordering = ('name',)