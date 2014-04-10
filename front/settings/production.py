from base import *  # NOQA


DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']


MEDIA_ROOT = BASE_DIR + '/media'
STATICFILES_DIRS = (
    BASE_DIR + '/front/static',
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'TEST_CHARSET': 'utf8',
        'TEST_DATABASE_COLLATION': 'utf8_general_ci',
    }
}


INSTALLED_APPS += (
    'gunicorn',
)


LOGGING = {
    'version': 1,
}
