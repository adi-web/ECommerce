
from django.contrib.auth.models import User
from django.db import models
from shopOnline.models import Item
# Create your models here.

class Order(models.Model):
    datetime=models.DateTimeField
    phoneNumber=models.CharField(max_length=200, db_index=True, blank=True)
    addressOrder=models.CharField(max_length=200, db_index=True, blank=True)
    userOrder=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    noteOrder=models.CharField(max_length=200, db_index=True, blank=True)
    totpay=models.FloatField(db_index=True, blank=True,default=0)


class OrderItem(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE,null=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    quantity=models.CharField(max_length=200,blank=True,default=0)
