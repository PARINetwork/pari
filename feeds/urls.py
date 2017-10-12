from django.conf.urls import patterns, url
from .feeds import AllFeed, ArticleFeed, AlbumFeed, \
    FaceFeed, ResourceFeed

urlpatterns = patterns('',
    url(r'^list/?$', 'feeds.feeds.feeds_list_page', name="feeds_list_page"),
    url(r'^all/?$', AllFeed(), name="all_feeds"),
    url(r'^articles/?$', ArticleFeed(), name="article_feeds"),
    url(r'^albums/?$', AlbumFeed(), name="album_feeds"),
    url(r'^faces/?$', FaceFeed(), name="face_feeds"),
    url(r'^resources/?$', ResourceFeed(), name="resource_feeds"),
)
