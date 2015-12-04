from django.shortcuts import render_to_response
import os,string,random
from django.template import RequestContext
from catelator.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse


def test1(request):
    print "there...."
    uid = request.session.get('uid','0')
    user = None
    if(uid != '0'):
        user = User.objects.get(pk = uid)
    return render_to_response("test/test1.html",{'user':user})


def test2(request):
    username = request.GET['username']
    content  = request.GET['content']
    return render_to_response("test/test2.html",{"username":username,"content":content},context_instance=RequestContext(request))