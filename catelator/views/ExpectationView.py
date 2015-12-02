from django.shortcuts import render_to_response
import os,string,random
from django.template import RequestContext
from catelator.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse

def go_add(request):
    print 'here..'
    p_all = Period.objects.all()
    c = {}
    c['p_all'] = p_all
    return render_to_response("expectation/expectation_input.html",c)

def deal_consumption(request):
    print 'ajax'
    walk = request.GET.get('walk')
    exercise = request.GET.get('exercise')
    print walk, exercise
    consum = float(walk) + float(exercise)
    return HttpResponse(consum)

@csrf_exempt
def expectation_add(request):
    print 'expectation_add'
    uid = request.session.get('uid','0')
    if(uid == '0'):
        return render_to_response("user/error.html")
    else :
        user = User.objects.get(pk = uid)
        span = request.POST.get("span")
        increment = request.POST.get('increment')
        consumption = request.POST.get('consumption')
        start_date = request.POST.get('start_date')
        print span, increment, consumption, start_date
        intake = float(increment) + float(consumption)
        period = Period.objects.get(pk = request.POST.get('peroid'))
        expectation = Expectation(span=span, increment=increment, consumption=consumption, intake=intake, start_date=start_date, user=user, period = period)
        expectation.save()
        c = {}
        c['expectation'] = expectation
        return HttpResponseRedirect("/catelator/expectation/expectation_list")
        # return render_to_response("expectation/expectation_list.html",c, context_instance=RequestContext(request))

def expectation_list(request):
    print "enter in expectation_list "
    expectation_all = Expectation.objects.all()
    c = {}
    c['expectation_all'] = expectation_all
    return render_to_response("expectation/expectation_list.html", c, context_instance=RequestContext(request))

#go to edit the expection page
def go_edit(request, expectation_id):
    expectation = Expectation.objects.get(pk = expectation_id)
    p_all = Period.objects.all()
    c = {}
    c['p_all'] = p_all
    c['expectation'] = expectation
    return render_to_response("expectation/expectation_input.html",c)

def delete (request, expectation_id):
    expectation = Expectation.objects.get (pk = expectation_id)
    expectation.delete()
    return HttpResponseRedirect("/catelator/expectation/expectation_list")

@csrf_exempt
def edit (request):
    uid = request.session.get('uid','0')
    if(uid == '0'):
        return render_to_response("user/error.html")
    else :
        user = User.objects.get(pk = uid)
        span = request.POST.get("span")
        increment = request.POST.get('increment')
        consumption = request.POST.get('consumption')
        start_date = request.POST.get('start_date')
        intake = float(increment) + float(consumption)
        period = Period.objects.get(pk = request.POST.get('peroid'))
        expectation_id = request.POST.get("expectation_id")
        expectation = Expectation.objects.get(pk = expectation_id)
        expectation.span = span
        expectation.increment = increment
        expectation.consumption = consumption
        expectation.intake = intake
        expectation.start_date = start_date
        expectation.user = user
        expectation.period = period
        expectation.save()
        return HttpResponseRedirect("/catelator/expectation/expectation_list")