from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
import datetime
from catelator.models import  *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response


def add_comment(request):
    uid  = request.session.get('uid','0')
    comment_context = request.GET.get("comment_context")
    status_id = request.GET.get("status_id")

    status_list = Status.objects.all()
    user = User.objects.get(pk = uid)
    status = Status.objects.get(pk = status_id)
    comment = Comment(status = status, user = user, comment_content = comment_context, content_date = timezone.now())
    comment.save()

    comment_list = Comment.objects.all()

    return render_to_response("comment/comment_add.html",{'comment_list':comment_list,'status':status,'status_list':status_list,'user':user})

def delete_comment(request):
    uid = request.session.get('uid','0')
    comment_id = request.GET.get("comment_id")
    status_id = request.GET.get("status_id")
    print uid, comment_id, status_id
    status_list = Status.objects.all()
    status = Status.objects.get(pk = status_id)
    user = User.objects.get(pk = uid)

    comment = Comment.objects.get(pk = comment_id)
    comment.delete()
    comment_list = Comment.objects.all()

    return render_to_response("comment/comment_add.html",{'comment_list':comment_list,'status':status,'status_list':status_list,'user':user})