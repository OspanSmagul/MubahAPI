from django.db import models 
 
 
class Company(models.Model):  
    id = models.IntegerField(primary_key = True)
    company_name = models.CharField(max_length=256, blank=True, null=True, default='') 
    brand_name = models.CharField(max_length=256, blank=True, null=True, default='') 
    address = models.CharField(max_length=512, blank=True, null=True, default='') 
    email = models.CharField(max_length=256, blank=True, null=True, default='') 
    site = models.CharField(max_length=256, blank=True, null=True, default='') 
    contact = models.CharField(max_length=256, blank=True, null=True, default='')
    logo = models.ImageField(upload_to='logos', null=True, blank=True)
    chicken_status = models.CharField(max_length=512, blank=True, null=True, default='')
    beaf_status = models.CharField(max_length=512, blank=True, null=True, default='')
    mutton_status = models.CharField(max_length=512, blank=True, null=True, default='')
    horsemeat_status = models.CharField(max_length=512, blank=True, null=True, default='')

    class Meta: 
        ordering = ('company_name',) 