from django.db import models

from DishModel import *
from UserModel import *

class UserOrder(models.Model):

    user = models.ForeignKey(User)
    dish = models.ForeignKey(Dish)
    order_date = models.DateField(default=None)

    def __unicode__(self):
        return self.order_date