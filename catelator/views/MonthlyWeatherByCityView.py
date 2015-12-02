from django.shortcuts import render_to_response
import os,string,random
from django.template import RequestContext
from catelator.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse
from chartit import DataPool,Chart

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
