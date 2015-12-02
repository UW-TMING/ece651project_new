from django.db import models
from UserModel import *
from PeriodModel import *

class Expectation(models.Model):
    span = models.IntegerField(default='0')
    increment = models.FloatField(max_length=10,default='0')
    consumption = models.FloatField(max_length=10,default='0')
    intake = models.FloatField(max_length=10,default='0')
    start_date = models.DateField(max_length=20,default=None)
    user = models.ForeignKey(User)
    period = models.ForeignKey(Period)


