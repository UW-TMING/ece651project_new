from django.db import models
from DishModel  import *

class ShoppingCart(models.Model):
    dish = models.ForeignKey(Dish)
    select = models.IntegerField(default=0)
    count = models.IntegerField(default=0)