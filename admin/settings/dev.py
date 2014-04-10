from base import *  # NOQA


DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


MEDIA_ROOT = BASE_DIR + '/media'
STATICFILES_DIRS = (
    BASE_DIR + '/admin/static',
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ATOMIC_REQUESTS': True,
    }
}


INSTALLED_APPS += (
    'debug_toolbar',
)


MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
