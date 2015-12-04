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
    return render_to_response("user/signIn.html")

@csrf_exempt
def register(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User(user_name=username,password=password,birth=timezone.now())
    user.save()
    return render_to_response("user/user_list.html",{'user':user},context_instance=RequestContext(request))

def go_login(request):
    return render_to_response("user/signIn.html")

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    print username,password
    try:
        user = User.objects.get(user_name=username,password=password)
    except:
        return HttpResponse("<p style='color:red'>login failed</p>")
    request.session["uid"] = user.pk
    print "--->",user
    return HttpResponseRedirect('/catelator/home')
    # return render_to_response('dish/dish_input.html',{},context_instance=RequestContext(request))

def logout(request):

    uid = request.session.get('uid','0')
    print "logout.....",uid
    if(uid != '0'):
        request.session['uid'] = '0'
        request.session['shop_cart'] = []
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

def main_page(request, possible_friend_id):
    uid = request.session.get('uid','0')
    user = User.objects.get(pk = uid )
    possible_firend = User.objects.get(pk = possible_friend_id)
    friends_list = Friends.objects.filter(follow = uid)
    status_list = Status.objects.filter(user = User.objects.get(pk = possible_friend_id))
    exist = 0
    status_exist = {}
    for status in status_list:
        statusupvote = StatusUpvote.objects.filter(status = status)
        for statusupvote_sub in statusupvote:
            if statusupvote_sub.user_id == uid:
                exist = 1
        status_exist[status.pk] = exist
        exist = 0

    comment_list = Comment.objects.filter(status__in = status_list)
    status_upvote_list = []
    for status_sub in status_list:
        status_upvote_list = status_upvote_list + list(StatusUpvote.objects.filter(status = status_sub)[:3])

    exist = 1
    for friend in friends_list:
        if friend.befollow.id == int(possible_friend_id):
            exist = 0
    friends_list = Friends.objects.filter(follow = possible_friend_id)

    picture_list = StatusPicture.objects.all()
    pictures = []
    for status2 in status_list:
        for picture in picture_list:
            if picture.status.pk == status2.pk:
                pictures.append(picture)
    condition = "self"
    return render_to_response("user/homePage.html",{'possible_firend':possible_firend,'exist':exist,'status_list':status_list,\
                                'comment_list':comment_list,'status_upvote_list':status_upvote_list,'status_exist':status_exist,\
                                'friends_list':friends_list,'user':user,'pictures':pictures,'condition':condition})

