# coding=utf8
from __future__ import unicode_literals

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'admin.home.views',
    url(r'^$', 'index', name='index'),
)
