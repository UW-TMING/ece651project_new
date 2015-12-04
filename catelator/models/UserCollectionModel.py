from django.db import models
from DishModel import *
from UserModel import *
from django.utils import timezone

class UserCollection(models.Model):
    user = models.ForeignKey(User)
    dish = models.ForeignKey(Dish)
    collection_date = models.DateField(default=None)