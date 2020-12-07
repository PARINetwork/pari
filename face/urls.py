from django.conf.urls import url
from django.views.generic import RedirectView

from .views import FaceList, FaceDetail

urlpatterns = [
                       url(r'^faces/$', RedirectView.as_view(url='/categories/faces/', permanent=True)),
                       url(r'^categories/faces/$', FaceList.as_view(), name='face-list'),
                       url(r'^categories/faces/(?P<alphabet>\w)/$', FaceDetail.as_view(),
                           name='face-detail'),
                       url(r'^categories/faces/(?P<alphabet>\w)/(?P<slug>[\w\-]+)/$', FaceDetail.as_view(),
                           name='face-detail-single'),
                       ]
