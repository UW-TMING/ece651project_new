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
from django.utils import timezone
import datetime

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

    reality = Reality (intake = intake, intake_date = intake_date,average_intake=expectation.intake, expectation = expectation)
    reality.save()
    c = {}
    c['reality'] = reality
    return render_to_response("reality/reality_list.html", c, context_instance=RequestContext(request))

def check_reality (request, expectation_id):
    if (expectation_id == 0):
        return HttpResponseRedirect("/catelator/expectation/expecation_go_add/")
    expectation = Expectation.objects.get (pk = expectation_id)
    print expectation.pk
    all_reality_byexid = Reality.objects.filter (expectation = expectation)
    c = {}
    c['all_reality_byexid'] = all_reality_byexid

    weatherdata = DataPool(
        series=[
            {
                'options':{'source': all_reality_byexid},
                'terms':['intake_date', 'intake','average_intake']
            }
        ]
    )
    #step 2: Create the Chart object
    cht = Chart(
        datasource = weatherdata,
        series_options = [
            {
                'options':{'type':'column','stacking':False},
                'terms':{
                    'intake_date':['intake','average_intake']
                }
            }
        ],

        chart_options = {
            'title' : {'text':'Real Intake And Average Intake'},
            'xAxis' : {
                'title' : {
                    'text' : 'Day'
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


def add_cart (request, dish_id):
    cart = request.session.get('shop_cart')
    if (cart == None):
        cart = []
    dish = Dish.objects.get (pk = dish_id)
    sc = ShoppingCart(dish=dish, select=0, count=1)
    # cart=[]
    cart.append(sc)
    request.session['shop_cart'] = cart
    return render_to_response("reality/show_cart.html", {"cart":cart}, context_instance=RequestContext(request))

def cart_deal (request):
    uid = request.session.get('uid','0')
    if(uid == '0'):
        return render_to_response("user/error.html")
    else :
        now = datetime.date.today()
        expectation = None
        for e in Expectation.objects.filter(user_id = uid):
            get_date = e.start_date
            if(now >= get_date and now <= get_date + datetime.timedelta(days=e.span)):
                expectation = e
        if(expectation == None):
            return HttpResponseRedirect("/catelator/expectation/expecation_go_add/")
        else:
            print "--->",expectation.intake
            content = request.GET.get("content")
            dish_ids = content.split("-")
            proteins = 0
            carbohydrates = 0
            vitamins = 0
            calories = 0
            for i in range(0,len(dish_ids)-1):
                dish = Dish.objects.get(pk = dish_ids[i])
                proteins = proteins + dish.protein
                carbohydrates = carbohydrates + dish.carbohydrates
                vitamins = vitamins + dish.vitamins
                calories = calories + dish.calories
            p1 = PieShow(content="protein", percent=proteins, percent1=proteins)
            p2 = PieShow(content="carbohydrates", percent=carbohydrates, percent1=carbohydrates)
            p3 = PieShow(content="vitamins", percent=vitamins, percent1=vitamins)
            PieShow.objects.all().delete()
            p1.save()
            p2.save()
            p3.save()

            c1 = ColumnShow(c_name=str(datetime.date.today()), average_calories=expectation.intake, selected_calories=calories)
            ColumnShow.objects.all().delete()
            c1.save()
            ds = DataPool(
            series=
                [{'options': {
                    'source': PieShow.objects.all()},
                  'terms': [
                    'content',
                    'percent',
                    'percent1']},

                  {'options': {
                    'source': ColumnShow.objects.all()},
                  'terms': [
                    'c_name',
                    'average_calories',
                    'selected_calories'
                    ]}
                 ])
            cht = Chart(
                datasource = ds,
                series_options =
                  [
                    {'options':{
                      'type': 'pie',
                      'center': [150, 50],
                        'size': '50%'},
                    'terms':{
                      'content': [
                        'percent']
                      }}
                      ,
                      {'options':{
                      'type': 'column',
                      'width':'10'},
                        'terms':{
                      'c_name': [
                        'average_calories',
                        'selected_calories']
                      }}],
                chart_options =
                  {'title': {
                       'text': 'Average calories and all calories'}},
                x_sortf_mapf_mts = [(None, None, False),(None, None, False)])
            c = {}
            c['weatherchart'] = cht
            return render_to_response("test/test5.html",c)

def del_from_cart(request, dish_id):
    cart = request.session.get('shop_cart')
    if (cart == None):
        return HttpResponseRedirect("/catelator/expectation/expecation_go_add/")
    else :
        print len(cart)
        for each in cart:
            if (each.dish.pk==long(dish_id)):
                cart.remove(each)
        request.session['shop_cart'] = cart
        return render_to_response("reality/show_cart.html", {"cart":cart}, context_instance=RequestContext(request))


def cart_deal_number(request):
    dish_id = request.GET.get('dish_id')
    number = request.GET.get('number')
    cart = request.session.get('shop_cart')
    if (cart == None):
        return HttpResponseRedirect("/catelator/expectation/expecation_go_add/")
    else :
        for each in cart:
            if (each.dish.pk==long(dish_id)):
                each.count = number
                break
        return HttpResponse()

def check_shopcart(request):
    cart = request.session.get('shop_cart')
    if (cart == None):
        return HttpResponseRedirect("/catelator/expectation/expecation_go_add/")
    else :
        return render_to_response("reality/show_cart.html", {"cart":cart}, context_instance=RequestContext(request))



