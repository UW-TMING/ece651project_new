from django.test import TestCase
from catelator.models.UserModel import *
import datetime
from django.core.urlresolvers import *
from django.utils import timezone
from catelator.models import *



class StatusTest(TestCase):
    def status_date_test(self):
        time = timezone.now() + datetime.timedelta(days=30)
        status = Status(status_date = time)
        self.assertEqual(status.was_published_recently(), True)
    def status_pk_exist_test(self):
        time = timezone.now() + datetime.timedelta(days=30)
        status = Status(status_date = time)
        self.assertEqual(status.status_pk_exist(), True)