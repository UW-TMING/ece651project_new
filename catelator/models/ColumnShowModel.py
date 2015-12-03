from django.db import models

class ColumnShow(models.Model):
    c_name = models.CharField(max_length=100,default=0)
    average_calories = models.FloatField(max_length=100,default=0)
    selected_calories = models.FloatField(max_length=100,default=0)