from django.shortcuts import render_to_response
import os,string,random
from django.template import RequestContext
from catelator.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse
from chartit import DataPool,Chart


def monthname(month_num):
    names ={1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
            7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    return names[month_num]

def weather_chart_view(request):
    print 'entering in weather_chart_view.'
    #step 1: create a DataPool with the data we want to retrieve
    weatherdata = DataPool(
        series=[
            {
                'options':{'source': MonthlyWeatherByCity.objects.all()},
                'terms':['month', 'houston_temp', 'boston_temp']
            }
        ]
    )
    #step 2: Create the Chart object
    cht = Chart(
        datasource = weatherdata,
        series_options = [
            {
                'options':{'type':'line','stacking':False},
                'terms':{
                    'month':['boston_temp', 'houston_temp']
                }
            }
        ],

        chart_options = {
            'title' : {'text':'Weather Data of Boston and Houston'},
            'xAxis' : {
                'title' : {
                    'text' : 'Month Number'
                }
            }
        }

    )
    return render_to_response("test/test3.html",{'weatherchart' : cht})


def test5(request):
    dish = Dish.objects.get(pk = 37)
    print "dish--->",dish
    p1 = PieShow(content="protein", percet=str(dish.protein))
    p2 = PieShow(content="carbohydrates", percet=str(dish.carbohydrates))
    p3 = PieShow(content="vitamins", percet=str(dish.vitamins))
    p1.save()
    p2.save()
    p3.save()

    ds = DataPool(
       series=
        [{'options': {
            'source': PieShow.objects.all() },
          'terms': [
            'content',
            'percent',
            'houston_temp']}
         ])

    cht = Chart(
        datasource = ds,
        series_options =
          [{'options':{
              'type': 'pie',
              'stacking': False},
            'terms':{
              'month': [
                'boston_temp',
                'houston_temp']
              }}],
        chart_options =
          {'title': {
               'text': 'Monthly Temperature of Boston'}},
        x_sortf_mapf_mts = (None, monthname, False))

    return render_to_response("test/test5.html",{'weatherchart' : cht})
