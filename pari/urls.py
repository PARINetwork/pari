import os

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.core.views import serve
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.images import urls as wagtailimages_urls

from author.views import add_translator, add_photographer
from core.views import PreviewOnEditPage, PreviewOnCreatePage
from search.views import admin_search

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),

    url(r'^admin/pages/search/$', admin_search),
    url(r'^admin/translators/add/$', add_translator),
    url(r'^admin/photographers/add/$', add_photographer),
    url(r'^admin/pages/add/(\w+)/(\w+)/(\d+)/preview/$', PreviewOnCreatePage.as_view()),
    url(r'^admin/pages/(\d+)/edit/preview/$', PreviewOnEditPage.as_view()),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^documents/', include(wagtaildocs_urls)),
]

urlpatterns += i18n_patterns(url(r'^parinews/', include('news.urls')),
                             url(r'^feeds/', include('feeds.urls')),
                             url(r'^', include('resources.urls')),
                             url(r'^article/', include('article.urls')),
                             url(r'^albums/', include('album.urls')),
                             url(r'^images/', include(wagtailimages_urls)),
                             url(r'^', include('article.urls')),
                             url(r'^', include('face.urls')),
                             url(r'^', include('category.urls')),
                             url(r'^', include('location.urls')),
                             url(r'^', include('search.urls')),
                             url(r'^', include('donation.urls')),
                             url(r'^', include('core.urls')),
                             url(r'', include(wagtail_urls)),
                             url(r'^(.*)/$', serve, name='wagtail_serve'),
                             )

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
