from django.db import models
from UserModel import *

class PieShow(models.Model):
    content = models.CharField(max_length=100,default=0)
    percent = models.FloatField(max_length=100,default=0)
    percent1 = models.FloatField(max_length=100,default=0)