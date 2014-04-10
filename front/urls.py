# coding=utf8
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^', include('front.home.urls', namespace='home')),
    url(r'^', include('front.auth.urls', namespace='auth')),
    url(r'^signup/', include('front.registration.urls', namespace='registration')),
    url(r'^mypage/', include('front.mypage.urls', namespace='mypage')),
)


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Static files
    urlpatterns += staticfiles_urlpatterns()

    # Media files
    urlpatterns += patterns(
        '',
        url(
            r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}
        )
    )
