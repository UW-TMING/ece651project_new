from django.db import models
from ExpectationModel import *

class Reality(models.Model):
    intake = models.FloatField(max_length=10,default='0')
    intake_date = models.CharField(max_length=50,default=None)
    expectation = models.ForeignKey(Expectation)

