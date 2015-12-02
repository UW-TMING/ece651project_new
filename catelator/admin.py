from django.contrib import admin

from catelator.models import *

admin.site.register(User)
admin.site.register(Dish)
admin.site.register(Period)
admin.site.register(MonthlyWeatherByCity)
admin.site.register(Article)