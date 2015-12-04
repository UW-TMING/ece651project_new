from django.db import models
from DishModel import *
from UserModel import *
from django.utils import timezone

class UserLike(models.Model):
    user = models.ForeignKey(User)
    dish = models.ForeignKey(Dish)
    like_date = models.DateField(default=None)