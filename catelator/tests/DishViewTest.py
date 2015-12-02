from catelator.views import DishView
import datetime
from django.core.urlresolvers import *
from django.utils import timezone
from django.test import TestCase

class DishViewTests(TestCase):

    def test_add_only_pic_name_and_later_path(self):
        pic_name = "\static\upload\images\19048168306qhlcd.jpg"
        response =self.client.get(reverse('/catelator/dish/dish_list',args=(pic_name,)))
        self.assertEqual(response.status_code,404)

    def test_add_without_anything(self):
        response =self.client.get(reverse('/catelator/dish/dish_list'))
        self.assertEqual(response,status_code=404)

    def test_add_only_have_dish_name(self):
        dish_name = "Alu Matar"
        response =self.client.get(reversed('/catelator/dish/dish_list',args=(dish_name,)))
        self.assertEqual(response,status_code=404)

    def test_add_only_composition(self):
        composition = "Oinion:100g;Beef:100g"
        response =self.client.get(reverse('/catelator/dish/dish_list',args=(composition,)))
        self.assertEqual(response.status_code,404)