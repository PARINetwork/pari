from django.conf.urls import url
from .views import site_search

urlpatterns = [
                       url(r'^search/', site_search, name='site_search'),
                       ]
