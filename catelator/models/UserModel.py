from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    pic = models.CharField(max_length=100,default="static/upload/images/default.jpg")
    gender = models.CharField(max_length=20,default='female')
    weight = models.FloatField(max_length=10,default='0')
    height = models.FloatField(max_length=10,default='0')
    birth = models.DateField(default=None)

    def __unicode__(self):
        return self.user_name