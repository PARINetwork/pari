from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


# Disable debug mode
DEBUG = False


# Domain names that this Django site can serve
ALLOWED_HOSTS = [u'staging.ruralindiaonline.org']

# Compress static files offline
# http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

try:
    from .local import *
except ImportError:
    pass

sentry_sdk.init(
    dsn="https://e87c857ac5c248e5b4868cfdd71a2cbf@sentry.io/1377604",
    environment='Staging',
    integrations=[DjangoIntegration()]
)
