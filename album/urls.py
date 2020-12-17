from django.conf.urls import url

from album.views import AlbumDetail, AlbumList, get_slide_detail, TaggedAlbumList


urlpatterns = [
        url(r'^$', AlbumList.as_view(), {'filter': 'all'}, name='album-list'),
        url(r'^tags/(?P<tag>[^/]+)/$', TaggedAlbumList.as_view(), {'filter': 'all'}, name='tagged-album-list'),
        url(r'^talking/$', AlbumList.as_view(), {'filter': 'talking'}, name='talking-album-list'),
        url(r'^other/$', AlbumList.as_view(), {'filter': 'other'}, name='other-album-list'),
        url(r'^(?P<slug>.+)/all/$', AlbumDetail.as_view(), name='image-collection-image-list'),
        url(r'^(?P<slug>.+).json/$', get_slide_detail, name='album_slide_detail'),
        url(r'^(?P<slug>.+)/$', AlbumDetail.as_view(), name='album-detail'),
]
