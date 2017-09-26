from .base import *


# Disable debug mode
DEBUG = False


# Domain names that this Django site can serve
ALLOWED_HOSTS = [u'staging.ruralindiaonline.org']

ENABLE_SITE_LOCALIZATION = True
# Compress static files offline
# http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

try:
    from .local import *
except ImportError:
    pass
