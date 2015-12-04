from django.db import models
from UserModel import *

class Friends (models.Model):
    follow = models.IntegerField(default = 0)
    befollow = models.ForeignKey(User,null = True)

    def __unicode__(self):
        return str(self.follow) + ' follow ' + str(self.befollow.id)