from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from .views import ResourceDetail, ResourceList, TaggedResourceList, \
    RoomResourceList, RackResourceList, ResourceListBySubject

urlpatterns = patterns('',
                       url(r'^library/$',
                           ResourceList.as_view(), name='resource-list'),
                       url(r'^library/tags/(?P<tag>[^/]+)/$',
                           TaggedResourceList.as_view(), name='tagged-resource-list'),

                       url(r'^library/search$',
                           'search.views.site_search', {'template': 'resources/search_results.html'},
                           name='resource-search'),

                       url(r'^library/resource/(?P<slug>[^/]+)/$',
                           ResourceDetail.as_view(), name='resource-detail'),

                       url(r'^library/room/(?P<slug>[^/]+)/$',
                           RoomResourceList.as_view(), name='room-resource-list'),
                       url(r'^library/room/(?P<room_slug>[^/]+)/(?P<rack_slug>[^/]+)/$',
                           RackResourceList.as_view(), name='rack-resource-list'),
                       url(r'^library/subject/(?P<slug>[^/]+)/$',
                           ResourceListBySubject.as_view(), name='resource-list-by-subject'),

                       url(r'^resources/(?P<slug>.+)/?$',
                           RedirectView.as_view(url='/library/resource/%(slug)s', permanent=True),
                           name='deprecated-resource-detail'),
                       url(r'^resources/?(?P<rest>.*)',
                           RedirectView.as_view(url='/library/%(rest)s', permanent=True),
                           name='deprecated-resource-list'),
)
