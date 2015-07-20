from django.conf.urls import patterns, url

from .views import ResourceDetail, ResourceList, ReportDetail

urlpatterns = patterns('',
                       url(r'^$', ResourceList.as_view(), name='resource-list'),
                       url(r'^(?P<slug>.+)/$', ResourceDetail.as_view(), name='resource-detail'),
                       url(r'^(?P<slug>.+)/report$', ReportDetail.as_view(), name='report-detail')
)
