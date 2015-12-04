from django.test import TestCase
from catelator.models.UserModel import *
import datetime
from django.core.urlresolvers import *
from django.utils import timezone

def create_time( days):

    time = timezone.now() + datetime.timedelta(days=days)
    return User(birth = time)

class UserModelTest(TestCase):
    def user_birth_is_before_today(self):
        the_day_after_today = create_time(1)
        response =self.client.get(reverse('user/error.html',args=(the_day_after_today,)))
        self.assertEqual(response,status_code=404)

    def user_birth_have_the_wrong_month(self):
        time = create_time(0)
        time.month = 13
        response =self.client.get(reverse('user/error.html',args=(time,)))
        self.assertEqual(response,status_code=404)

    def user_have_wrong_name(self):
        user_name = "%%matt"
        response =self.client.get(reverse('user/error.html',args=(user_name,)))
        self.assertEqual(response,status_code=404)