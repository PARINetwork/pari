from .base import *


# Disable debug mode
DEBUG = False


# Domain names that this Django site can serve
ALLOWED_HOSTS = [u'staging.ruralindiaonline.org']

# Compress static files offline
# http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

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
        }
    },
}

try:
    from .local import *
except ImportError:
    pass
