from .base import *
import logging

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', u'development.ruralindiaonline.org']

INSTALLED_APPS += (
    'nplusone.ext.django',
    'django_nose',
)

MIDDLEWARE_CLASSES += (
    'nplusone.ext.django.NPlusOneMiddleware',
)

NPLUSONE_LOGGER = logging.getLogger('nplusone')
NPLUSONE_LOG_LEVEL = logging.WARN

LOGGING = {
    'version': 1,
    'disable_existing_logger': False,
    'formatters':{
        'verbose': {
            'format': '%(asctime)s [%(levelname)s] %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'filename': '/vagrant/logs/pari.log',
            'maxBytes': 1024 * 1024 * 10, # 10MB,
            'backupCount': 20,
            'formatter': 'verbose'
        }
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
        'nplusone': {
            'handlers': ['console'],
            'level': 'WARN',
        }
    },
}


try:
    from .local import *
except ImportError:
    pass
