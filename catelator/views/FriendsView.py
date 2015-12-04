from django.shortcuts import render_to_response
import os,string,random
from django.template import RequestContext
from catelator.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
import re
import sys

@csrf_exempt
def add_friend(request):
    uid = request.session.get('uid','0')
    exist = int(request.POST.get('exist'))
    friend_id = int(request.POST.get('friend_id'))

    user = User.objects.get(pk = friend_id)
    if exist:
        friend = Friends(follow = uid, befollow = user)
        friend.save()
        return HttpResponseRedirect("/catelator/user/main_page/"+str(friend_id)+"/")
    else:
        friend1 = Friends.objects.get(follow = uid, befollow = user)
        friend1.delete()
        return HttpResponseRedirect("/catelator/user/main_page/"+str(friend_id)+"/")

def go_to_add(request):
    return render_to_response("user/addFriends.html")

def friends_finding(uid):
    user_friend_list = []
    for friend in Friends.objects.all():
        if friend.follow == uid:
            user_friend_list.append(friend.befollow.pk)
    print "---",user_friend_list
    user_available_list = list(User.objects.exclude(pk__in = user_friend_list))
    random.shuffle( user_available_list )
    return user_available_list

def search_friends(request):
    uid = request.session.get('uid','0')
    userinformation = str(request.GET.get('userinformation'))
    m = re.match(r'(\d+)',userinformation)
    if m :
        try:
            print type(userinformation)
            befinders = list(User.objects.filter(pk = m.group(1)))
        except ObjectDoesNotExist:
            befinders = None
        return render_to_response("user/addFriends.html",{'search_type':1,'befinders':befinders})
    else :
        try:
            befinders = User.objects.filter(user_name = str(userinformation))
        except ObjectDoesNotExist:
            befinders = None
        return render_to_response("useR/addFriends.html",{'search_type':1,'befinders':list(befinders)})

def test_friends(request):
    return render_to_response("user/friend_search.html",{'search_type':0})

