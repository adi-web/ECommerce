from django.db import models


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=200, db_index=True, blank=True)

class Item(models.Model):
    name = models.CharField(max_length=1200, db_index=True)
    image = models.ImageField(null=True, upload_to='images/', blank=True)
    price = models.FloatField(default=0)
    available = models.BooleanField(default=True)
    description = models.CharField(default="csdc", max_length=10000, db_index=True)
    categories=models.ForeignKey(Categories,on_delete=models.CASCADE,default=None)



