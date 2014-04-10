from django.conf.global_settings import *  # NOQA
from core.settings.base import *  # NOQA


WSGI_APPLICATION = 'admin.wsgi.application'


ROOT_URLCONF = 'admin.urls'


TEMPLATE_DIRS = (
    BASE_DIR + '/admin/templates',
)


INSTALLED_APPS += ()


TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
)


MIDDLEWARE_CLASSES += (
    'django_sorting.middleware.SortingMiddleware',
    'pagination.middleware.PaginationMiddleware',
)


AUTH_USER_MODEL = 'account.Administrator'
LOGIN_URL = '/login'
LOGOUT_URL = '/logout'
LOGIN_REDIRECT_URL = '/'


PAGINATION_INVALID_PAGE_RAISES_404 = True
