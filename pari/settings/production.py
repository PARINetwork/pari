from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


# Disable debug mode

DEBUG = False

# Compress static files offline
# http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True


# Use Redis as the cache backend for extra performance
# (requires the django-redis-cache package):
# http://wagtail.readthedocs.org/en/latest/howto/performance.html#cache

# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.cache.RedisCache',
#         'LOCATION': '127.0.0.1:6379',
#         'KEY_PREFIX': 'pari',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
#         }
#     }
# }


try:
    from .local import *
except ImportError:
    pass

sentry_sdk.init(
    dsn="https://e87c857ac5c248e5b4868cfdd71a2cbf@sentry.io/1377604",
    environment='Prod',
    integrations=[DjangoIntegration()]
)
