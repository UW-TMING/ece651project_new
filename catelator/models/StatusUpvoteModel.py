from django.db import models
from StatusModel import *

class StatusUpvote(models.Model):
    user_id = models.IntegerField(default = 0)
    user_name = models.CharField(max_length = 20,default = '')
    upvote_date = models.DateField(auto_now = True)
    status = models.ForeignKey(Status)

    def __unicode__(self):
        return str(self.user_id) #+ '--' + self.upvote_date