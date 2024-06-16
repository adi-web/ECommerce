from django.conf import settings
# Create your models here.
from django.db import models

from shopOnline.models import Item


class CommentItem(models.Model):
    description=models.CharField(max_length=1000,db_index=True,blank=True)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=0)
    itemComment=models.ForeignKey(Item,on_delete=models.CASCADE,null=True,blank=True,default=1)


