from django.conf.urls import patterns, url

from .views import FaceList, FaceDetail

urlpatterns = patterns('faces.views',
        url(r'^categories/faces/$', FaceList.as_view(), name='face-list'),
        url(r'^categories/faces/(?P<alphabet>\w)/$', FaceDetail.as_view(),
            name='face-detail'),
        url(r'^categories/faces/(?P<alphabet>\w)/(?P<slug>[\w\-]+)/$', FaceDetail.as_view(),
            name='face-detail-single'),
)
