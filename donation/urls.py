from django.conf.urls import patterns, url


urlpatterns = patterns('donation.views',
    url(r'^donate/$', 'donate_form', name='donate_form'),
    url(r'^donate/success/$', 'donate_success', name='donate_success'),
    url(r'^donate/webhook/$', 'instamojo_webhook', name='instamojo_webhook'),
    url(r'^donate/checkout$', 'razorpay_checkout', name='razorpay_checkout'),
    url(r'^donate/rp-verify/$', 'razorpay_verify', name='razorpay_verify'),
    url(r'^donate/log-modal-close/$', 'log_modal_close', name='log_modal_close'),
)
