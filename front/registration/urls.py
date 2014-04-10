# coding=utf8
from __future__ import unicode_literals

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'front.registration.views',
    url(r'^$', 'index', name='index'),
    url(r'^thanks$', 'thanks', name='thanks'),
)
