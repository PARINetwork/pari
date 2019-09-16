from django.conf.urls import patterns, url


urlpatterns = patterns('core.views',
    url(r'^$', 'home_page', name='home-page'),

    url(r'^(?P<slug>contribute)/?$', 'contribute', name='contribute'),
    url(r'^contribute/(?P<slug>guidelines)/$', 'static_page', name='static_page'),

    url(r'^(?P<slug>about)/$', 'static_page', name='static_page'),
    url(r'^about/(?P<slug>pari\-teachers\-students)/$', 'static_page', name='static_page'),
    url(r'^about/(?P<slug>about\-the\-editor)/$', 'static_page', name='static_page'),
    url(r'^about/(?P<slug>acknowledgements)/$', 'static_page', name='static_page'),

    url(r'^legal/(?P<slug>terms\-and\-conditions)/$', 'static_page', name='static_page'),
    url(r'^legal/(?P<slug>copyright)/$', 'static_page', name='static_page'),

    url(r'^contact-us/$', 'contact_us', name='contact_us'),
    url(r'^(?P<slug>donate)/$', 'static_page', name='static_page'),

    url(r'^pages/guidelines/$', 'guidelines', name='guidelines'),
    url(r'^pages/pari-teachers-students/$', 'pari_teachers_students', name='pari_teachers_students'),
    url(r'^pages/contribute-to-faces/$', 'contribute_to_faces', name='contribute_to_faces'),
    url(r'^pages/donate/$', 'donate', name='donate'),
    url(r'^pages/about/$', 'about', name='about'),
    url(r'^pages/acknowledgements/$', 'acknowledgements', name='acknowledgements'),
    url(r'^pages/about-the-editor/$', 'founders', name='founders'),
    url(r'^pages/(?P<slug>.+)/$', 'static_page', name='static_page'),
    url(r'^sitemap\.xml$', 'sitemap_index', name='sitemap_index'),
    url(r'^sitemap-(?P<year>\d+)\.xml', 'sitemap_year', name='sitemap_year'),
)

'''
urlpatterns += patterns('',
    # To handle unicode in the slugs.
    url(r'^(.*?)$', 'wagtail.wagtailcore.views.serve', name='wagtail_serve'),
)
'''