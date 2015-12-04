from django.http import HttpResponse
from django.template import RequestContext
import datetime
from catelator.models import  *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response


def upvote(request):
    uid = request.session.get('uid','0')
    status_id = request.GET.get('status_id')
    like = request.GET.get('like')
    condition = str(request.GET.get('condition'))
    possible = int(request.GET.get('possible'))
    possible_friend = User.objects.get(pk = possible)
    status = Status.objects.get(pk = status_id)
    print like,status.pk,possible,condition
    if like == 'Upvote':
        username = User.objects.get(pk = uid).user_name
        upvote_date = timezone.now()
        upvote = StatusUpvote(user_id = uid, user_name = username, upvote_date = upvote_date,status = Status.objects.get(pk = status_id))
        upvote.save()
        status.sum += 1
        status.save()
    if like == 'Upvoted':
        print  uid, status
        StatusUpvote.objects.filter(user_id = uid, status = status).delete()
        print "asf"
        status.sum -= 1
        status.save()

    print 123
    if condition == "self":
        status_list = Status.objects.filter(user = User.objects.get(pk = possible))
        print status_list

    if condition == "all":
        status_list = Status.objects.all()
    print 2222
    exist = 0
    status_exist = {}

    for status1 in status_list:
        statusupvote = StatusUpvote.objects.filter(status = status1)
        for statusupvote_sub in statusupvote:
            if statusupvote_sub.user_id == uid:
                exist = 1
        status_exist[status1.pk] = exist
        exist = 0

    return render_to_response("status/upvote_success.html",{'status_list':status_list,'status_exist':status_exist,\
                            'status_now':status,'possible_friend':possible_friend,'condition':condition})