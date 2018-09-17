from django.db import models

# Create your models here.
from __future__ import unicode_literals
from django.db import models

from django.conf import settings

from decimal import Decimal
from datetime import datetime

# Create your models here.


class Admins_DB_renote(models.Model):
    user_id = models.EmailField(max_length=60,blank=True,default = '')
    user_email = models.EmailField(max_length=160,blank=True,default = '')
    user_pass = models.CharField(max_length=100,blank=True,default = '')
    firstname = models.CharField(max_length=40,blank=True,default = '')
    lastname = models.CharField(max_length =80,blank=True,default = '')
    created_date = models.DateTimeField(auto_now_add=True)
    mobile_no = models.CharField(max_length =40,blank=False)
    ListofOperations = models.CharField(max_length=15000,blank=True,default = '')
    photo = models.FileField(upload_to=settings.IMGUPLOAD_URL)
    devices_types_list = models.CharField(max_length=500,blank=True,default = '')
    devices_id_list = models.CharField(max_length=15000,blank=True,default = '')
    devices_last_login_times = models.CharField(max_length=2500,blank=True,default = '')
    assigned_token = models.CharField(max_length=1500,blank=True,default = '')
    assigned_token_stamps = models.DateTimeField(blank=True,default = '1900-01-01 10:10')
