from django.shortcuts import render_to_response
import os,string,random
from django.template import RequestContext
from catelator.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

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
    userinformation = int(request.GET.get('userinformation'))
    search_type = request.GET.get('search_type')
    print search_type, userinformation,User.objects.get(pk = userinformation )
    if search_type == 'ID':
        try:
            befinders = list(User.objects.filter(pk = userinformation))
        except ObjectDoesNotExist:
            befinders = None
        return render_to_response("user/friend_search.html",{'search_type':1,'befinders':befinders})
    if search_type == 'Name':
        print "name"
        try:
            befinders = User.objects.filter(user_name = userinformation)
        except ObjectDoesNotExist:
            befinders = None
        return render_to_response("use/friend_search.html",{'search_type':1,'befinders':list(befinders)})

def test_friends(request):
    return render_to_response("user/friend_search.html",{'search_type':0})

