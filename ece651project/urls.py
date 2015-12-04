
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^catelator/',include('catelator.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
