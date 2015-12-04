from django.contrib import admin

from catelator.models import *

admin.site.register(User)
admin.site.register(Dish)
admin.site.register(Comment)
admin.site.register(StatusUpvote)
admin.site.register(StatusPicture)
admin.site.register(Status)
admin.site.register(Friends)

# class NewsAdmin(admin.ModelAdmin):
#     list_dislpay='news_title'
#
#
#
# admin.site.register(Status,NewsAdmin)