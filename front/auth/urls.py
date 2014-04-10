# coding=utf8
from __future__ import unicode_literals

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'front.auth.views',
    url(r'^login$', 'login', name='login'),
    url(r'^logout$', 'logout', name='logout'),
)
