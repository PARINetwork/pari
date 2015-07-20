from django.conf.urls import patterns, url

from .views import CategoriesList, CategoryDetail

urlpatterns = patterns('category.views',
    url(r'^categories/(?P<slug>.+)/$', CategoryDetail.as_view(), name='category-detail'),
    url(r'^categories/$', CategoriesList.as_view(), name='category-list'),
)
