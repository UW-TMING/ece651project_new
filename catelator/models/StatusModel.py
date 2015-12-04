from django.db import models
from UserModel import *
from ckeditor.fields import RichTextField
from django.utils import timezone


class Status(models.Model):
    status_content = models.CharField(max_length = 255)
    status_date = models.DateTimeField(auto_now=False)
    sum  = models.IntegerField(default = 0)
    news_content = RichTextField("content")
    user = models.ForeignKey(User, null=True)
    def publish_date(self):
        now = timezone.now()
        return self.status_date <= now
    def publish_pk_exist(self):
        return  self.pk != 0
    def __unicode__(self):
        return str(self.pk) + '  ' + self.status_content
