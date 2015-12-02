from django.db import models

class Material(models.Model):
    material_name = models.CharField(max_length=20)
    calorie = models.FloatField(max_length=10,default='0')
    protein = models.FloatField(max_length=10,default='0')
    vitamin = models.FloatField(max_length=10,default='0')
    carbohydrate = models.FloatField(max_length=10,default='0')

    def __unicode__(self):
        return self.material_name
