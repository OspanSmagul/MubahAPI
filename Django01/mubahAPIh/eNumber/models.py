from django.db import models

# Create your models here.

class eNumber(models.Model): 
    number = models.CharField(max_length=32, blank=True, default='') 
    name = models.CharField(max_length=128, blank=True, default='') 
    description = models.CharField(max_length=1024, blank=True, default='') 
    status = models.CharField(max_length=1024, blank=True, default='') 
    
 
    class Meta: 
        ordering = ('name',) 