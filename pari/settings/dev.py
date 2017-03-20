from .base import *


DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', u'development.ruralindiaonline.org']

try:
    from .local import *
except ImportError:
    pass
