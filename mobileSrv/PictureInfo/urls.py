__author__ = 'shixk'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('PictureInfo.views',
    url(r'^get_pic$', 'get_pic'),
    url(r'^get_basetime$', 'get_basetime'),
)