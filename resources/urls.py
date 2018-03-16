from django.conf.urls import patterns, url

from .views import ResourceDetail, ResourceList, ReportDetail

urlpatterns = patterns('',
                       url(r'^resources/?$', ResourceList.as_view(), name='resource-list'),
                       url(r'^resources/(?P<slug>.+)/$', ResourceDetail.as_view(), name='resource-detail'),
                       url(r'^(?P<slug>.+)/report$', ReportDetail.as_view(), name='report-detail')
)
