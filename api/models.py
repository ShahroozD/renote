from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User
from django.conf import settings
import django

from decimal import Decimal
from datetime import datetime

# Create your models here.
class Users_Db_Renote(models.Model):
    user_id = models.CharField(max_length =40,blank=False)
    user_email = models.EmailField(max_length=160,blank=True,default = '')
    user_pass = models.CharField(max_length=50,blank=False,default = '')
    username = models.CharField(max_length=80,blank=True,default = '')
    status = models.CharField(max_length=40,blank=True,default = '')
    isverified = models.IntegerField(default = 0,blank=True)
    private = models.IntegerField(default = 0,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    photo = models.FileField(upload_to=settings.IMGUPLOAD_URL)
    firebase_notif_ID = models.CharField(max_length =10000,blank=True,default = '')
    onesignal_notif_ID = models.CharField(max_length =10000,blank=True,default = '')
    devices_types_list = models.CharField(max_length=500,blank=True,default = '')
    devices_id_list = models.CharField(max_length=15000,blank=True,default = '')
    devices_last_login_times = models.CharField(max_length=2500,blank=True,default = '')
    last_login_time = models.CharField(max_length=2500,blank=True,default = '')
    assigned_token = models.CharField(max_length=1500,blank=True,default = '')
    assigned_token_stamps = models.DateTimeField(blank=True,null=True,default = '1900-01-01 10:10')
    confirm_sms_val = models.CharField(max_length=10,blank=True)
    confirm_sms_time_stamp = models.DateTimeField(blank=True,null=True,default = '1900-01-01 10:10')
    user_credit = models.FloatField(default = 0,blank=True)
    is_black = models.BooleanField(blank=True,default = 0)
    introduction_code = models.CharField(max_length=20,blank=True,default = '')
    who_introduction_code = models.CharField(max_length=20,blank=True,default = '')
    state = models.CharField(max_length=90,blank=True,default = '')
    city = models.CharField(max_length=90,blank=True,default = '')
    mount_cost = models.IntegerField(default = 0,blank=True)

    def __unicode__(self):
        return self.fullname



class Users_Tokens_Db_Renote(models.Model):
    assigned_token = models.CharField(max_length=60,blank=False,unique=True)
    user = models.ForeignKey('Users_Db_Renote', on_delete=models.CASCADE)
    assigned_token_stamps = models.DateTimeField(blank=True,null=True,default = django.utils.timezone.now)
    assigned_token_last_time = models.DateTimeField(blank=True,null=True,default = django.utils.timezone.now)
    device = models.CharField(max_length=100,blank=True,default = '')
    celery_task_id=models.CharField(max_length=50,blank=True,null=True,default='')

    def __unicode__(self):
        return self.user





class Note_Db_Renote(models.Model):
    tracking_code = models.CharField(max_length=60,blank=False,unique=True)
    user = models.ForeignKey('Users_Db_Renote', on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True,null=True,default = django.utils.timezone.now)
    note = models.CharField(max_length=400,blank=True,default = '')
    photo = models.FileField(upload_to=settings.IMGUPLOAD_URL)
    group = models.CharField(max_length=100,blank=True,default = '')
    hashtag = models.CharField(max_length=90,blank=True,default = '')
    weekday_name = models.CharField(max_length=100,blank=True,default = '')
    celery_task_id=models.CharField(max_length=50,blank=True,null=True,default='')

    def __unicode__(self):
        return self.tracking_code


class Likes_DB(models.Model):
    user = models.ForeignKey('Users_Db_Renote', on_delete=models.CASCADE)
    post = models.ForeignKey('Note_Db_Renote', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    celery_task_id=models.CharField(max_length=50,blank=True,null=True,default='')








# ==============================================================================
# ==============================================================================
# ==============================================================================



class FollowingManager(models.Manager):
    """ Following manager """

    def followers(self, keyword):
        return self.filter(followee=user).all()


    def following(self, keyword):
        return self.filter(follower=user).all()

    #
    #
    # def add_follower(self, follower, followee):
    #     """ Create 'follower' follows 'followee' relationship """
    #     if follower == followee:
    #         raise ValidationError("Users cannot follow themselves")
    #
    #     relation, created = self.get_or_create(follower=follower, followee=followee)
    #
    #     if created is False:
    #         raise AlreadyExistsError("User '%s' already follows '%s'" % (follower, followee))
    #
    #     return relation
    #
    #
    #
    # def remove_follower(self, follower, followee):
    #     """ Remove 'follower' follows 'followee' relationship """
    #     try:
    #         rel = self.get(follower=follower, followee=followee)
    #         # rel = Follow.objects.get(follower=follower, followee=followee)
    #         rel.delete()
    #
    #         return True
    #     except Follow.DoesNotExist:
    #         return False
    #
    #
    #
    # def follows(self, follower, followee):
    #     """ Does follower follow followee? Smartly uses caches if exists """
    #
    #     try:
    #         self.get(follower=follower, followee=followee)
    #         return True
    #     except Follow.DoesNotExist:
    #         return False
    #






class Follow_DB(models.Model):
    """ Model to represent Following relationships """
    follower = models.ForeignKey('Users_Db_Renote', on_delete=models.CASCADE, related_name='follower')
    followee = models.ForeignKey('Users_Db_Renote', on_delete=models.CASCADE, related_name='followee')
    date = models.DateTimeField(default=django.utils.timezone.now)
    accepted = models.IntegerField(default = 1,blank=True)
    celery_task_id=models.CharField(max_length=50,blank=True,null=True,default='')


    objects = FollowingManager()

    # def __unicode__(self):
    #     return self.title

    # class Meta:
    #     verbose_name = _('Following Relationship')
    #     verbose_name_plural = _('Following Relationships')
    #     unique_together = ('follower', 'followee')

    # def __str__(self):
    #     return "User #%s follows #%s" % (self.follower_id, self.followee_id)
    #
    # def save(self, *args, **kwargs):
    #     # Ensure users can't be friends with themselves
    #     if self.follower == self.followee:
    #         raise ValidationError("Users cannot follow themselves.")
    #     super(Follow, self).save(*args, **kwargs)
