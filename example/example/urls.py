# coding: utf-8

from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('gallery.urls', namespace='gallery', app_name='gallery')),
]
