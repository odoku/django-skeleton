# coding=utf8
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns(
    '',
    url(r'^', include('admin.home.urls', namespace='home')),
    url(r'^', include('admin.auth.urls', namespace='auth')),
)


if settings.DEBUG:
    # Django Admin
    from django.contrib import admin
    admin.autodiscover()
    urlpatterns += patterns('', url(r'^admin/', include(admin.site.urls)))

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
