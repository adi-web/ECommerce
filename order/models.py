import datetime

from django.contrib.auth.models import User
from django.db import models
from shopOnline.models import Item
# Create your models here.

class Order(models.Model):
    date=models.DateField(default=datetime.date.today())
    phoneNumber=models.CharField(max_length=200, db_index=True, blank=True)
    addressOrder=models.CharField(max_length=200, db_index=True, blank=True)
    userOrder=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    noteOrder=models.CharField(max_length=200, db_index=True, blank=True)
    totpay=models.FloatField(db_index=True, blank=True,default=0)
    stateOrder=models.BooleanField(default=True)


class OrderItem(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE,null=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    quantity=models.CharField(max_length=200,blank=True,default=0)
    stateItem=models.BooleanField(default=True)
    payQuantity=models.FloatField(default=0,db_index=True,blank=True)


    def delete(self, *args, **kwargs):
        # Adjust the total payment of the related order
        self.order.totpay -= self.item.price
        self.stateItem=False
        self.order.save()
        self.save()
        # Call the original delete method
        #super().delete(*args, **kwargs)
