from django.shortcuts import render_to_response
import os,string,random
from django.template import RequestContext
from catelator.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse

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
def add(request):
    dish_name = request.POST['dish_name']
    recipe = request.POST['recipe']
    composition = request.POST['composition']
    # print dish_name,'--',recipe
    f = request.FILES.get('pic_name')
    later_path = 'static/upload/images/'+get_number()+'.jpg'
    write_pic(f,later_path)
    uid = request.session.get('uid','0')
    user = User.objects.get(id = uid)
    dish = Dish(dish_name=dish_name,recipe=recipe,composition=composition,pic=later_path,creator=user)
    dish.save()
    # c = {}
    # c["dish"] = dish
    # return render_to_response('dish/show_dish.html',c,context_instance=RequestContext(request))
    return HttpResponseRedirect('/catelator/dish/dish_list')

def dish_list(request):
    uid = request.session.get('uid','0')
    print 'uid:',uid
    if(uid != '0'):
        user = User.objects.get(pk = uid)
        print user.user_name
        dish_lists = Dish.objects.filter(creator__pk = uid)
        c = {}
        print '-->',len(dish_lists)
        c['dish_lists'] = dish_lists
        c['user'] = user
        return render_to_response('dish/dish_list.html',c,context_instance=RequestContext(request))
    else :
        return render_to_response('user/error.html',{},context_instance=RequestContext(request))

def edit(request,dish_id):
    uid = request.session.get('uid','0')
    if(uid == '0'):
        return render_to_response("user/error.html")
    else :
        dish = Dish.objects.get(pk = dish_id)
        user = User.objects.get(pk = uid)
        c = {}
        c['dish'] = dish
        c['user'] = user
        return render_to_response('dish/dish_input.html',c,context_instance=RequestContext(request))

def show_detail(request,dish_id):
    dish = Dish.objects.get(pk = dish_id)
    c = {}
    c['dish'] = dish
    return render_to_response('dish/show_dish.html',c,context_instance=RequestContext(request))

def delete(request,dish_id):
    dish = Dish.objects.get(pk = dish_id)
    dish.delete()
    return HttpResponseRedirect('/catelator/dish/dish_list')

# user collect the dish
def collect(request,dish_id):
    uid = request.session.get('uid')
    user = User.objects.get(pk = uid)
    dish = Dish.objects.get(pk = dish_id)
    c = UserCollection(user = user ,dish = dish ,collection_date = timezone.now())
    c.save()
    return HttpResponseRedirect('/catelator/dish/dish_list')

def like(request,dish_id):
    uid = request.session.get('uid')
    user = User.objects.get(pk = uid)
    dish = Dish.objects.get(pk = dish_id)
    l = UserLike(user = user ,dish = dish ,like_date = timezone.now())
    l.save()
    return HttpResponseRedirect('/catelator/dish/dish_list')

@csrf_exempt
def update(request):
    dishid = request.POST['dish_id']
    dish = Dish.objects.get(pk = dishid)
    dish.dish_name = request.POST['dish_name']
    dish.composition = request.POST['composition']
    dish.recipe = request.POST['recipe']
    dish.status_quality = '0'
    f = request.FILES.get('pic_name')
    if(f == None):
        dish.save()
    else:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        oldpath = os.path.join(BASE_DIR, dish.pic)
        os.remove(oldpath)
        later_path = 'static/upload/images/'+get_number()+'.jpg'
        write_pic(f,later_path)
        dish.pic = later_path
        dish.save()
    return HttpResponseRedirect('/catelator/dish/dish_list')

def go_dish_input(request):
    uid = request.session.get('uid','0')
    if(uid == '0'):
        return render_to_response("user/error.html")
    else :
        user = User.objects.get(pk = uid)
        c = {}
        c['user'] = user
        return render_to_response('dish/dish_input.html',c)