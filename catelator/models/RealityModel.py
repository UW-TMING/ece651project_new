from django.db import models
from ExpectationModel import *

class Reality(models.Model):
    intake = models.FloatField(max_length=10,default='0')
    intake_date = models.DateField(max_length=20,default=None)
    expectation = models.ForeignKey(Expectation)

    def __unicode__(self):
        return self.intake,'-',self.intake_date