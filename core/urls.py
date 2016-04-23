from django.conf.urls import patterns, url


urlpatterns = patterns('core.views',
    url(r'^$', 'home_page', name='home-page'),

    url(r'^(?P<slug>contribute)/$', 'contribute', name='contribute'),
    url(r'^contribute/(?P<slug>guidelines)/$', 'static_page', name='static_page'),

    url(r'^(?P<slug>about)/$', 'static_page', name='static_page'),
    url(r'^about/(?P<slug>pari\-teachers\-students)/$', 'static_page', name='static_page'),
    url(r'^about/(?P<slug>about\-the\-editor)/$', 'static_page', name='static_page'),
    url(r'^about/(?P<slug>acknowledgements)/$', 'static_page', name='static_page'),

    url(r'^legal/(?P<slug>terms\-and\-conditions)/$', 'static_page', name='static_page'),
    url(r'^legal/(?P<slug>copyright)/$', 'static_page', name='static_page'),

    url(r'^contact-us/$', 'contact_us', name='contact_us'),
    url(r'^(?P<slug>donate)/$', 'static_page', name='static_page'),

    url(r'^pages/(?P<slug>.+)/$', 'static_page', name='static_page'),
)

urlpatterns += patterns('',
    # To handle unicode in the slugs.
    url(r'^(.*?)$', 'wagtail.wagtailcore.views.serve', name='wagtail_serve'),
)
