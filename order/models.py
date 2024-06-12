from django.db import models
from shopOnline.models import Item
# Create your models here.

#class Address(models.Model):
    #nameAddress=models.CharField(max_length=200, db_index=True, blank=True)
    #number=models.CharField(max_length=200, db_index=True, blank=True)
    #city=models.CharField(max_length=200, db_index=True, blank=True)
    #cap=models.CharField(max_length=200, db_index=True, blank=True)



class Order(models.Model):
    datetime=models.DateTimeField
    phoneNumber=models.CharField(max_length=200, db_index=True, blank=True)
    addressOrder=models.CharField(max_length=200, db_index=True, blank=True)
    item=models.ManyToManyField(Item)

