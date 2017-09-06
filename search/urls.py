from django.conf.urls import patterns, url

urlpatterns = patterns('search.views',
                       url(r'^search/', 'site_search', name='site_search'),
                       )
