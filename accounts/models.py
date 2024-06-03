from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=250,db_index=True,blank=False)
    addressCustomer = models.CharField(max_length=250,db_index=True, blank=False)
    numberAddress = models.CharField(max_length=250,db_index=True, blank=False)
    city = models.CharField(max_length=250,db_index=True, blank=False)
    cap = models.CharField(max_length=250,db_index=True, blank=False)


