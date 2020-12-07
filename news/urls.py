from django.conf.urls import url

from news.views import PariNewsView

urlpatterns = [
                url(r'^$', PariNewsView.as_view(), name='pari-news')
]
