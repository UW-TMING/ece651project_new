from django.db import models
from UserModel import *

class Dish(models.Model):
    STATUS_QUALITY = (
        ('0','during_approve'),
        ('1','not_approved'),
        ('2','approved'),
    )
    dish_name = models.CharField(max_length=20)
    recipe = models.TextField(null=True)
    composition = models.CharField(max_length=100,null=True)
    pic = models.CharField(max_length=100,null=True)
    status_quality = models.CharField(max_length=1,choices=STATUS_QUALITY,default='0')
    creator = models.ForeignKey(User)
    orders = models.ManyToManyField(User,through='UserOrder',related_name="uorder")
    likes = models.ManyToManyField(User,through="UserLike",related_name="ulike")
    collections = models.ManyToManyField(User,through="UserCollection",related_name="ucollect")

    def __unicode__(self):
        return self.dish_name