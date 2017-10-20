from django.conf.urls import patterns, url

from .views import ArticleDetail, ArticleList, ArchiveDetail, AuthorArticleList
from location.views import LocationDetail
urlpatterns = patterns('article.views',
    url(r'^authors/(?P<slug>.+)/$',AuthorArticleList.as_view(), name='author-detail'),
    url(r'^authors/(?P<slug>.+)/?$', AuthorArticleList.as_view(), name='author-detail'),
    url(r'^articles/$', ArticleList.as_view(), {'filter': 'article-list'}, name='article-list'),
    url(r'^articles/(?P<slug>.+)/$', ArticleDetail.as_view(), name='article-detail'),
    url(r'^articles/(?P<slug>.+)/?$', ArticleDetail.as_view(), name='article-detail'),
    url(r'^locations/(?P<slug>.+)/$', LocationDetail.as_view(), name='location-detail'),
    url(r'^locations/(?P<slug>.+)/?$', LocationDetail.as_view(), name='location-detail'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d+)/$', ArchiveDetail.as_view(), name='archive-detail'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d+)/?$', ArchiveDetail.as_view(), name='archive-detail'),
)

