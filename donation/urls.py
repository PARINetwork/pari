from django.conf.urls import url
from .views import donate_form, donate_success, instamojo_webhook, razorpay_checkout, razorpay_verify, log_modal_close, \
    bank_transfer, dd_cheque

urlpatterns = [
    url(r'^donate/$', donate_form, name='donate_form'),
    url(r'^donate/success/$', donate_success, name='donate_success'),
    url(r'^donate/webhook/$', instamojo_webhook, name='instamojo_webhook'),
    url(r'^donate/checkout$', razorpay_checkout, name='razorpay_checkout'),
    url(r'^donate/rp-verify/$', razorpay_verify, name='razorpay_verify'),
    url(r'^donate/log-modal-close/$', log_modal_close, name='log_modal_close'),
    url(r'^donate/bank-transfer-details/$', bank_transfer, name='bank-transfer-details'),
    url(r'^donate/cheque-dd-details/$', dd_cheque, name='cheque-dd-details'),
]
