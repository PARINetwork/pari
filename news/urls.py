from django.conf.urls import patterns, url

from news.views import PariNewsView

urlpatterns = patterns('news.views',
                url(r'^$', PariNewsView.as_view(), name='pari-news')
)
