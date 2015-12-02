from django.shortcuts import render_to_response
import os,string,random
from django.template import RequestContext
from catelator.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse
from chartit import DataPool,Chart
import json

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

@csrf_exempt
def add_reality (request):
    print 'there... add_reality '
    intake = request.POST.get("intake")
    intake_date = request.POST.get("intake_date")
    expectation_id = request.POST.get ("expectation_id")
    print intake, intake_date, expectation_id
    expectation = Expectation.objects.get(pk = request.POST.get("expectation_id"))

    reality = Reality (intake = intake, intake_date = intake_date, expectation = expectation)
    reality.save()
    c = {}
    c['reality'] = reality
    return render_to_response("reality/reality_list.html", c, context_instance=RequestContext(request))

def check_reality (request, expectation_id):
    print 'check_reality-->', expectation_id
    expectation = Expectation.objects.get (pk = expectation_id)
    print expectation.pk
    all_reality_byexid = Reality.objects.filter (expectation = expectation)
    c = {}
    c['all_reality_byexid'] = all_reality_byexid

    weatherdata = DataPool(
        series=[
            {
                'options':{'source': all_reality_byexid},
                'terms':['intake_date', 'intake']
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
                    'intake_date':['intake']
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
    c['weatherchart'] = cht
    return render_to_response("reality/reality_all_exid.html", c, context_instance=RequestContext(request))


    # return render_to_response("reality/reality_all_exid.html", c, context_instance=RequestContext(request))

def go_add_reality (request, expectation_id):
    c = {}
    c['expectation_id'] = expectation_id
    return render_to_response("reality/reality_input.html", c, context_instance=RequestContext(request))