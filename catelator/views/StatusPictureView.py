from django.shortcuts import render_to_response
import os,string,random
from django.template import RequestContext
from catelator.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
#from catelator.views.DishView import get_number,write_pic

def get_number():
    s = str(random.uniform(1,1000000)).replace('.','')
    s = s+string.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)).replace(' ','')
    return s

def write_pic(f,later_path):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    mypath = os.path.join(BASE_DIR, later_path)
    with open(mypath, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@csrf_exempt
def add_picture(request):
    uid = request.session.get('uid','0')
    f = request.FILES.get('fileUp')
    later_path = 'static/upload/images/'+get_number()+'.jpg'
    write_pic(f,later_path)
    user = User.objects.get(id = uid)
    picture = StatusPicture(path = later_path, status = None)
    picture.save()
    picture_none_list = StatusPicture.objects.filter(status = None)
    print picture_none_list
    return HttpResponseRedirect("/catelator/news/status_all")
    #return render_to_response('status/status_add.html',{'picture_none_list':picture_none_list})