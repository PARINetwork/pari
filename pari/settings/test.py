from .base import *

ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'test_pari',
        'USER': 'pari',
        'PASSWORD': 'pari',
        'HOST': 'localhost',  # Set to empty string for localhost.
        'PORT': '',  # Set to empty string for default.
        'CONN_MAX_AGE': 600,  # number of seconds database connections should persist for
        'TEST': {
            'NAME': 'test_pari',
        },
    }
}
