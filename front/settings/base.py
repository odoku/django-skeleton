from __future__ import unicode_literals

from core.settings.base import *  # NOQA


WSGI_APPLICATION = 'front.wsgi.application'


ROOT_URLCONF = 'front.urls'


TEMPLATE_DIRS = (
    BASE_DIR + '/front/templates',
)


INSTALLED_APPS += ()


AUTH_USER_MODEL = 'account.User'
LOGIN_URL = '/login'
LOGOUT_URL = '/logout'
LOGIN_REDIRECT_URL = '/mypage'
