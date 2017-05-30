from .base import *
import logging

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', u'development.ruralindiaonline.org']

INSTALLED_APPS += (
    'nplusone.ext.django',
)

MIDDLEWARE_CLASSES += (
    'nplusone.ext.django.NPlusOneMiddleware',
)

NPLUSONE_LOGGER = logging.getLogger('nplusone')
NPLUSONE_LOG_LEVEL = logging.WARN

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'nplusone': {
            'handlers': ['console'],
            'level': 'WARN',
        },
    },
}


try:
    from .local import *
except ImportError:
    pass
