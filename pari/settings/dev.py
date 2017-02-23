from .base import *


DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ALLOWED_HOSTS = [ '0.0.0.0', '127.0.0.1', 'localhost' ]

try:
    from .local import *
except ImportError:
    pass
