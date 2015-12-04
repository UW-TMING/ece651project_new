from django.db import models
from StatusModel import *
from UserModel import *


class Comment(models.Model):
    comment_content = models.CharField(max_length = 255, default = None)
    content_date = models.DateField(auto_now = True)
    user = models.ForeignKey(User,null = True)
    status = models.ForeignKey(Status)

    def __unicode__(self):
        return str(self.pk) +' ' +str(self.user_id) + '--' + self.comment_content

