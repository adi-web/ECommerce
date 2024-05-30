from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(null=True,upload_to='images/', blank=True)
    quantityAvailable = models.IntegerField(default=10)
    price = models.FloatField(default=0)
    available = models.BooleanField(default=True)
    description = models.CharField(default="csdc",max_length=2000, db_index=True)



