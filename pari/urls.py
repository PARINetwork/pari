import os

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailsearch import urls as wagtailsearch_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtailimages import urls as wagtailimages_urls


urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),

    url(r'^admin/pages/search/$', 'search.views.admin_search'),
    url(r'^admin/translators/add/$', 'author.views.add_translator'),
    url(r'^admin/photographers/add/$', 'author.views.add_photographer'),
    url(r'^admin/pages/(\d+)/edit/preview/$', 'core.views.page_preview'),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^parinews/', include('news.urls')),
    url(r'^feeds/', include('feeds.urls')),

    url(r'^resources/', include('resources.urls')),
    url(r'^article/', include('article.urls')),
    url(r'^albums/', include('album.urls')),

    url(r'^images/', include(wagtailimages_urls)),

    url(r'^', include('article.urls')),
    url(r'^', include('face.urls')),
    url(r'^', include('category.urls')),
    url(r'^', include('location.urls')),
    url(r'^', include('search.urls')),

    url(r'^', include('core.urls')),

    url(r'', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
