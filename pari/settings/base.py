"""
Django settings for pari project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# coding: utf-8
from os.path import abspath, dirname, join

from django.utils.translation import ugettext_lazy as _

# Absolute filesystem path to the Django project directory:
PROJECT_ROOT = dirname(dirname(dirname(abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vcg^g$-6bce@3hk+bmiyn^exoe4r()+a9g%ypo7p(+fy*q*8em'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://ruralindiaonline.org'

# Application definition

INSTALLED_APPS = (
    'overextends',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.contrib.sites',

    'compressor',
    'taggit',
    'modelcluster',

    'core',
    'location',
    'author',
    'category',
    'article',
    'album',
    'face',
    'feeds',
    'resources',
    'search',
    'news',
    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtaildocs',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailusers',
    'wagtail.wagtailsites',
    'wagtail.wagtailimages',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsearch',
    'wagtail.wagtailredirects',
    'wagtail.wagtailforms',
    'wagtail.contrib.modeladmin',
    'wagtailtinymce',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'pari.urls'
WSGI_APPLICATION = 'pari.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# PostgreSQL (Recommended, but requires the psycopg2 library and Postgresql development headers)
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'pari',
        'USER': 'pari',
        'PASSWORD': 'pari',
        'HOST': 'localhost',  # Set to empty string for localhost.
        'PORT': '',  # Set to empty string for default.
        'CONN_MAX_AGE': 600,  # number of seconds database connections should persist for
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

ENABLE_SITE_LOCALIZATION = False
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Asia/Calcutta'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

MEDIA_ROOT = join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'


# Wagtail settings

WAGTAIL_SITE_NAME = "pari"

# Use Elasticsearch as the search backend for extra performance and better search results:
# http://wagtail.readthedocs.org/en/latest/howto/performance.html#search
# http://wagtail.readthedocs.org/en/latest/core_components/search/backends.html#elasticsearch-backend
#
WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'search.custom_elasticsearch.CustomElasticsearchSearchBackend',
        'INDEX': 'pari',
        'ATOMIC_REBUILD': True,
        'TIMEOUT': 30,
    },
}
WAGTAILADMIN_RICH_TEXT_EDITORS = {
    'default': {
        'WIDGET': 'wagtail.wagtailadmin.rich_text.HalloRichTextArea'
    },
    'hallo': {
        'WIDGET': 'article.rich_text.CustomHalloRichTextArea',
    },
    'hallo_for_quote': {
        'WIDGET': 'article.rich_text.CustomHalloRichTextArea',
        'OPTIONS': {
            "plugins": {
                "halloformat": {},
                "halloheadings": {"formatBlocks": ['p']},
                "hallorequireparagraphs": {}
            }
        }
    },
    'hallo_for_paragraph': {
        'WIDGET': 'article.rich_text.CustomHalloRichTextArea',
        'OPTIONS': {
            "plugins": {
                "halloformat": {},
                "halloheadings": {"formatBlocks": ['p', 'h2', 'h3', 'h4', 'h5']},
                "hallolists": {},
                "hallohr": {},
                "halloreundo": {},
                "hallowagtaillink": {},
                "hallorequireparagraphs": {}
            }
        }
    },
    'tinymce': {
        'WIDGET': 'wagtailtinymce.rich_text.TinyMCERichTextArea',
    },
    'tinymce_paragraph': {
        'WIDGET': 'wagtailtinymce.rich_text.TinyMCERichTextArea',
        'OPTIONS': {
            'buttons': [
                [
                    ['undo', 'redo'],
                    ['formatselect'],
                    ['bold', 'italic'],
                    ['bullist', 'numlist'],
                    ['hr'],
                    ['link', 'unlink'],
                    ['fullscreen'],
                ]
            ]
        }
    },
    'tinymce_quote': {
        'WIDGET': 'wagtailtinymce.rich_text.TinyMCERichTextArea',
        'OPTIONS': {
            'buttons': [
                [
                    ['undo', 'redo'],
                    ['bold', 'italic'],
                    ['fullscreen'],
                ]
            ]
        }
    },
}


TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
WAGTAILIMAGES_IMAGE_MODEL = 'core.AffixImage'
# Whether to use face/feature detection to improve image cropping - requires OpenCV
WAGTAILIMAGES_FEATURE_DETECTION_ENABLED = False
WAGTAIL_USAGE_COUNT_ENABLED = True
WAGTAILSEARCH_RESULTS_TEMPLATE = "search/search_results.html"

# Flag to show modular content panel in article admin page
MODULAR_ARTICLE = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

# Custom settings
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
    ('text/typescript', 'tsc {infile} --out {outfile}'),
    ('text/x-sass', 'sassc {infile} {outfile}'),
    ('text/x-scss', 'sassc --scss {infile} {outfile}'),
)

COMPRESS_ENABLED = False

COMPRESS_PARSER = 'compressor.parser.HtmlParser'
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

# India Map Center
MAP_CENTER = (23, 80)

CONTACT_EMAIL_RECIPIENTS = [
]

DONATE_EMAIL_RECIPIENTS = CONTACT_EMAIL_RECIPIENTS

SOUNDCLOUD_SETTINGS = {
    "API_URL": "https://api.soundcloud.com",
    "CLIENT_ID": "",
    "CLIENT_SECRET": "",
    "USERNAME": "",
    "PASSWORD": ""
}


STATE_CHOICES = (
    (_("Andaman and Nicobar Islands"), _("Andaman and Nicobar Islands")),
    (_("Andhra Pradesh"), _("Andhra Pradesh")),
    (_("Arunachal Pradesh"), _("Arunachal Pradesh")),
    (_("Assam"), _("Assam")),
    (_("Bihar"), _("Bihar")),
    (_("Chandigarh"), _("Chandigarh")),
    (_("Chhattisgarh"), _("Chhattisgarh")),
    (_("Dadra and Nagar Haveli"), _("Dadra and Nagar Haveli")),
    (_("Daman and Diu"), _("Daman and Diu")),
    (_("National Capital Territory of Delhi"), _("National Capital Territory of Delhi")),
    (_("Goa"), _("Goa")),
    (_("Gujarat"), _("Gujarat")),
    (_("Haryana"), _("Haryana")),
    (_("Himachal Pradesh"), _("Himachal Pradesh")),
    (_("Jammu and Kashmir"), _("Jammu and Kashmir")),
    (_("Jharkhand"), _("Jharkhand")),
    (_("Karnataka"), _("Karnataka")),
    (_("Kerala"), _("Kerala")),
    (_("Lakshadweep"), _("Lakshadweep")),
    (_("Madhya Pradesh"), _("Madhya Pradesh")),
    (_("Maharashtra"), _("Maharashtra")),
    (_("Manipur"), _("Manipur")),
    (_("Meghalaya"), _("Meghalaya")),
    (_("Mizoram"), _("Mizoram")),
    (_("Nagaland"), _("Nagaland")),
    (_("Odisha"), _("Odisha")),
    (_("Puducherry"), _("Puducherry")),
    (_("Punjab"), _("Punjab")),
    (_("Rajasthan"), _("Rajasthan")),
    (_("Sikkim"), _("Sikkim")),
    (_("Tamil Nadu"), _("Tamil Nadu")),
    (_("Telangana"), _("Telangana")),
    (_("Tripura"), _("Tripura")),
    (_("Uttar Pradesh"), _("Uttar Pradesh")),
    (_("Uttarakhand"), _("Uttarakhand")),
    (_("West Bengal"), _("West Bengal")),
)

SOCIAL = {
    "FACEBOOK": "PARINetwork",
    "TWITTER": "PARINetwork",
    "GITHUB_REPO": "PARINetwork/pari",
    "GOOGLE_ANALYTICS_ID": "UA-49439949-1",
    "YOUTUBE": "PARInetwork",
    "SOUND_CLOUD": "ruralindia"
}

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

# https://www.loc.gov/standards/iso639-2/php/code_list.php
LANGUAGES = (
    ("en", _("English")),
    ("as", _("Assamese")),
    ("bn", _("Bengali")),
    ("gu", _("Gujarati")),
    ("hi", _("Hindi")),
    ("kn", _("Kannada")),
    ("ml", _("Malayalam")),
    ("mr", _("Marathi")),
    ("lus", _("Mizo")),
    ("or", _("Odia")),
    ("pa", _("Punjabi")),
    ("te", _("Telugu")),
    ("ta", _("Tamil")),
    ("ur", _("Urdu")),
)

SITE_ID = 1

SITE_TITLE = ""

# Template configuration

from django.conf import global_settings

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join(PROJECT_ROOT, 'templates'),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
                'django.core.context_processors.request',
                'core.context_processors.settings',
            ),
        },
    },
]

INSTAMOJO = {
    "DONATE_URL": "",
    "SALT": "",
}

GOOGLE_MAP_KEY = ""

LOCALE_PATHS = (
    join(PROJECT_ROOT, 'locale'),
)
