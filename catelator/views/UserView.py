from django.shortcuts import render_to_response
import os
from django.template import RequestContext
from catelator.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from catelator.views.DishView import get_number,write_pic

def index(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    project_path = os.path.join(BASE_DIR,'templates')
    return render_to_response("user/index.html",{"project_path":project_path})

def go_register(request):
    return render_to_response("user/user_input.html")

@csrf_exempt
def register(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User(user_name=username,password=password,birth=timezone.now())
    user.save()
    return render_to_response("user/user_list.html",{'user':user},context_instance=RequestContext(request))

def go_login(request):
    return render_to_response("user/user_login.html")

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        user = User.objects.get(user_name=username,password=password)
    except:
        return HttpResponse("<p style='color:red'>login failed</p>")
    request.session["uid"] = user.pk
    return HttpResponseRedirect('/catelator/home')
    # return render_to_response('dish/dish_input.html',{},context_instance=RequestContext(request))

def logout(request):
    uid = request.session.get('uid','0')
    if(uid != '0'):
        del request.session['uid']
    return HttpResponseRedirect('/catelator/home')

def information(request):
    uid = request.session.get('uid','0')
    if(uid == '0'):
        return render_to_response("user/error.html")
    else :
        user = User.objects.get(pk = uid)
        c = {}
        c['user'] = user
        return render_to_response("catelator/pages/information.html",c)

def go_check_information(request):
    uid = request.session.get('uid','0')
    if(uid == '0'):
        return render_to_response("user/error.html")
    else :
        user = User.objects.get(pk = uid)
        c = {}
        c['user'] = user
        return render_to_response("user/check_information.html",c,context_instance=RequestContext(request))

def go_edit(request,user_id):
    user = User.objects.get(pk = user_id)
    c = {}
    c['user'] = user
    return render_to_response("user/edit_information.html",c,context_instance=RequestContext(request))

def go_complete(request,user_id):
    user = User.objects.get(pk = user_id)
    c = {}
    c['user'] = user
    return render_to_response("user/edit_information.html",c,context_instance=RequestContext(request))

@csrf_exempt
def complete_information(request):
    print 'here'
    height = request.POST['height']
    weight = request.POST['weight']
    gender = request.POST['gender']
    birth  = request.POST['birth']
    uid = request.POST['uid']

    if (uid == '0') :
        return render_to_response("user/error.html",{},context_instance=RequestContext(request))
    else :
        user = User.objects.get(pk = uid)
        user.height = height
        user.weight = weight
        user.gender = gender
        user.birth  = birth
        f = request.FILES.get('pic')
        if (f != None):
            later_path = 'static/upload/images/'+get_number()+'.jpg'
            write_pic(f,later_path)
            user.pic = later_path
        user.save()
        return HttpResponseRedirect("/catelator/user/go_check_information")

@csrf_exempt
def edit_information(request):
    height = request.POST['height']
    weight = request.POST['weight']
    gender = request.POST['gender']
    birth  = request.POST['birth']
    uid = request.POST['uid']
    if (uid == '0') :
        return HttpResponse("user/error.html")
    else :
        user = User.objects.get(pk = uid)
        user.height = height
        user.weight = weight
        user.gender = gender
        user.birth  = birth
        f = request.FILES.get('pic')
        print 'there-->',f
        if (f != None) :
            print 'entring '
            if(user.pic != ''):
                # print 'yes'
                BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                oldpath = os.path.join(BASE_DIR, user.pic)
                if os.path.exists(oldpath):
                    os.remove(oldpath)
            later_path = 'static/upload/images/'+get_number()+'.jpg'
            write_pic(f,later_path)
            user.pic = later_path
        user.save()
        return HttpResponseRedirect("/catelator/user/go_check_information")


def go_change_password(request,user_id,message=''):
    if(user_id == '0'):
        return render_to_response("user/error.html")
    else :
        user = User.objects.get(pk = user_id)
        c = {}
        c['user'] = user
        c['message'] = message
        return render_to_response("user/change_password.html",c,context_instance=RequestContext(request))

@csrf_exempt
def change_password(request):
    user_id = request.POST['user_id']
    print 'change --- > here'
    if (user_id == '0') :
        return render_to_response("user/error.html")
    else :
        oldpassword = request.POST['oldpassword']
        newpassword1 = request.POST['newpassword1']
        newpassword2 = request.POST['newpassword2']
        user = User.objects.get(pk = user_id)
        if(user.password != oldpassword):
            message = 'your oldpassword is wrong!'
        elif (newpassword1 != newpassword2):
            message = 'your new password is not equal for the two times input !'
        else :
            user.password = newpassword1
            user.save()
            message = 'change password successfully !'
        newpath = "/catelator/user/go_change_password/"+user_id+"/"+message
        return HttpResponseRedirect(newpath)