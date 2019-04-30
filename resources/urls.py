from django.conf.urls import patterns, url

from .views import ResourceDetail, ResourceList, ReportDetail, TaggedResourceList

urlpatterns = patterns('',
                       url(r'^resources/?$', ResourceList.as_view(), name='resource-list'),
                       url(r'^resources/tags/(?P<tag>[^/]+)/?$', TaggedResourceList.as_view(), name='tagged-resource-list'),
                       url(r'^resources/(?P<slug>.+)/$', ResourceDetail.as_view(), name='resource-detail'),
                       url(r'^(?P<slug>.+)/report$', ReportDetail.as_view(), name='report-detail')
)
