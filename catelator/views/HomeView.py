from django.shortcuts import render_to_response
import os,string,random
from django.template import RequestContext
from catelator.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse

def home(request):
    uid = request.session.get('uid','0')
    user = None
    if(uid != '0'):
        user = User.objects.get(pk = uid)
    return render_to_response("catelator/pages/index.html",{'user':user})

def recipe(request):
    uid = request.session.get('uid','0')
    user = None
    if(uid != '0'):
        dish_lists = Dish.objects.filter(status_quality='2')
        user = User.objects.get(pk = uid)
        c = {}
        c['user'] = user
        c['dish_lists'] = dish_lists
        return render_to_response("catelator/pages/recipe.html",c)
    else :
        return render_to_response("user/error.html")



