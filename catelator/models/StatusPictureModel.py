from django.db import models
from UserModel import *
from StatusModel import *


class StatusPicture(models.Model):
    path = models.CharField(max_length=100,default="static/upload/images/default.jpg")
    status = models.ForeignKey(Status,null=True)

    def __unicode__(self):
        return str(self.pk)
