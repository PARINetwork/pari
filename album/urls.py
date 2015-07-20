from django.conf.urls import patterns, url

from album.views import AlbumDetail, AlbumList


urlpatterns = patterns('album.views',
        url(r'^$', AlbumList.as_view(), {'filter': 'all'}, name='album-list'),
        url(r'^talking/$', AlbumList.as_view(), {'filter': 'talking'}, name='talking-album-list'),
        url(r'^other/$', AlbumList.as_view(), {'filter': 'other'}, name='other-album-list'),

        url(r'^(?P<slug>.+)/all/$', AlbumDetail.as_view(), name='image-collection-image-list'),
        url(r'^(?P<slug>.+)/$', AlbumDetail.as_view(), name='album-detail'),
)
