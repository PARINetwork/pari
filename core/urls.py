from django.conf.urls import url, include
import core.views as views


urlpatterns = [
    url(r'^$', views.home_page, name='home-page'),

    url(r'^(?P<slug>contribute)/?$', views.contribute, name='contribute'),
    url(r'^contribute/(?P<slug>guidelines)/$', views.static_page, name='static_page'),

    url(r'^(?P<slug>about)/$', views.static_page, name='static_page'),
    url(r'^about/(?P<slug>pari\-teachers\-students)/$', views.static_page, name='static_page'),
    url(r'^about/(?P<slug>about\-the\-editor)/$', views.static_page, name='static_page'),
    url(r'^about/(?P<slug>acknowledgements)/$', views.static_page, name='static_page'),

    url(r'^legal/(?P<slug>terms\-and\-conditions)/$', views.static_page, name='static_page'),
    url(r'^legal/(?P<slug>copyright)/$', views.static_page, name='static_page'),

    url(r'^contact-us/$', views.contact_us, name='contact_us'),
    url(r'^(?P<slug>donate)/$', views.static_page, name='static_page'),

    url(r'^pages/guidelines/$', views.guidelines, name='guidelines'),
    url(r'^pages/pari-teachers-students/$', views.pari_teachers_students, name='pari_teachers_students'),
    url(r'^pages/contribute-to-faces/$', views.contribute_to_faces, name='contribute_to_faces'),
    url(r'^pages/donate/$', views.donate, name='donate'),
    url(r'^pages/about/$', views.about, name='about'),
    url(r'^pages/acknowledgements/$', views.acknowledgements, name='acknowledgements'),
    url(r'^pages/about-the-editor/$', views.founders, name='founders'),
    url(r'^pages/(?P<slug>.+)/$', views.static_page, name='static_page'),
    url(r'^sitemap\.xml$', views.sitemap_index, name='sitemap_index'),
    url(r'^sitemap-(?P<year>\d+)\.xml', views.sitemap_year, name='sitemap_year'),
]
