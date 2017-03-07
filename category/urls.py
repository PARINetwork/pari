from django.conf.urls import patterns, url

from .views import CategoriesList, GalleryDetail, StoryDetail

urlpatterns = patterns('category.views',
    url(r'^gallery/categories/(?P<slug>.+)/$', GalleryDetail.as_view(), name='gallery-detail'),
    url(r'^stories/categories/(?P<slug>.+)/$', StoryDetail.as_view(), name='story-detail'),
    url(r'^categories/$', CategoriesList.as_view(), name='category-list'),
)
