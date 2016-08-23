from django.conf.urls import patterns, url

from .views import LocationList, LocationDetail


urlpatterns = patterns('',
    url(r'^map/$', LocationList.as_view(), name='map-list'),
    url(r'^locations/(?P<slug>.+)/$', LocationDetail.as_view(), name='location-detail'),
)
