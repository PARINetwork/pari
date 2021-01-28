from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


# Disable debug mode
DEBUG = True


# Domain names that this Django site can serve
ALLOWED_HOSTS = [
    u'staging.ruralindiaonline.org',
    u'ruralindiaonline.org'
]

# Compress static files offline
# http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

try:
    from .local import *
except ImportError:
    pass

import os

PARI_LOGLEVEL = os.environ.get('PARI_LOGLEVEL', 'info').upper()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '[%(asctime)s][%(levelname)s] %(name)s '
                      '%(filename)s:%(funcName)s:%(lineno)d | %(message)s',
            'datefmt': '%H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': PARI_LOGLEVEL,
            'class': 'logging.FileHandler',
            'filename': os.environ.get('DJANGO_LOGFILE', '/var/log/pari-django.log'),
            'formatter': 'console'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
        'pari': {
            'level': PARI_LOGLEVEL,
            'propagate': True,
        },
    }
}

sentry_sdk.init(
    dsn="https://e87c857ac5c248e5b4868cfdd71a2cbf@sentry.io/1377604",
    environment='Staging',
    integrations=[DjangoIntegration()]
)
