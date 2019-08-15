from django.conf.urls import patterns, url

from .views import CategoriesList, GalleryDetail, StoryDetail

urlpatterns = patterns('category.views',
    url(r'^categories/$', CategoriesList.as_view(), name='category-list'),
    url(r'^categories/(?P<slug>.+)/$', StoryDetail.as_view(), name='category-detail'),
    url(r'^stories/categories/(?P<slug>.+)/$', StoryDetail.as_view(), name='story-detail'),
    url(r'^gallery/categories/(?P<slug>.+)/$', GalleryDetail.as_view(), name='gallery-detail'),
    url(r'^gallery/$', 'gallery_home_page', name='gallery-home-page')
)
