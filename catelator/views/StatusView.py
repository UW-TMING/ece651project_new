from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
import datetime
from catelator.models import  *
from catelator.views import FriendsView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
import os,string,random

#@csrf_exempt
def all_status(request):
    uid = request.session.get('uid','0')
    user = User.objects.get(pk = uid)
    friends = Friends.objects.filter(follow = uid)[:9]
    user_available_list = FriendsView.friends_finding(uid)[:9]

    status_list = Status.objects.all().order_by('-status_date')

    exist = 0
    status_exist = {}
    for status in status_list:
        statusupvote = StatusUpvote.objects.filter(status = status)
        for statusupvote_sub in statusupvote:
            if statusupvote_sub.user_id == uid:
                exist = 1
        status_exist[status.pk] = exist
        exist = 0

    picture_list = StatusPicture.objects.all()
    pictures = []
    status_list1 = Status.objects.filter(user = User.objects.get(pk = uid))
    for status2 in status_list1:
        for picture in picture_list:
            if picture.status:
                if picture.status.pk == status2.pk:
                    pictures.append(picture)

    comment_list = Comment.objects.all()
    status_upvote_list = []
    for status_sub in status_list:
        status_upvote_list = status_upvote_list + list(StatusUpvote.objects.filter(status = status_sub)[:3])
        picture_none_list = StatusPicture.objects.filter(status = None)
    return render_to_response('catelator/pages/news1.html',{'status_list':status_list,'comment_list':comment_list,\
                            'status_upvote_list':status_upvote_list,'status_exist':status_exist,'friends':friends,\
                            'user':user,'user_available_list':user_available_list,'pictures':pictures,'picture_list':picture_list,'picture_none_list':picture_none_list},context_instance=RequestContext(request))

@csrf_exempt
def new_status(request):
    uid = request.session.get('uid','0')
    status_context = request.POST.get('status_context')
    user = User.objects.get(pk = uid)
    status = Status(status_date= timezone.now(), user = user, sum = 0 , status_content = status_context)
    status.save()
    print status.pk,StatusPicture.objects.filter(status = None)
    StatusPicture.objects.filter(status = None).update(status = status )
    print "finish"
    return HttpResponseRedirect("/catelator/news/status_all/")



def add_status(request):
    return render_to_response('status/status_add.html')


def set_status(request):
    picture_start = StatusPicture.objects.count()
    session.setAttribute("picture_start", picture_start);
    return HttpResponse()

def share_status(request):
    print "entry"
    print request.GET.get('comment_context')
    uid = request.session.get('uid','0')
    user = User.objects.get(pk = uid)
    status_id = request.GET.get('status_id')
    print "--",status_id
    comment_context = str(request.GET.get('comment_context')) +" // From :" + user.user_name
    status = Status.objects.get(pk = status_id)
    status.pk = None
    status.user = user
    status.status_content = comment_context + status.status_content
    status.status_date = timezone.now()
    status.sum = 0
    status.save()
    print "exit"
    return HttpResponse()



