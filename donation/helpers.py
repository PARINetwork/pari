# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import send_mail
from django.template import Context
from django.template.loader import render_to_string


class DonationOptions(object):
    class Amount(object):
        Rs500 = '500'
        Rs1000 = '1000'
        Rs2000 = '2000'
        OTHER = 'Other'
        CHOICES = (
            (Rs500,  u'₹ 500'),
            (Rs1000, u'₹ 1000'),
            (Rs2000, u'₹ 2000'),
            (OTHER, u''),
        )

    class Frequency(object):
        M = 'Monthly'
        Y = 'Yearly'
        ONE_TIME = 'ONE-TIME'
        MODEL_CHOICES = (
            (M, 'Monthly'),
            (Y, 'Yearly'),
        )
        FORM_CHOICES = MODEL_CHOICES + ((ONE_TIME, 'One-time'),)


def send_acknowledgement_mail(payment_context):
    email_msg = render_to_string('donation/acknowledgement_mail.html', Context(payment_context))
    send_mail(
        'We have received your donation', None,
        settings.DEFAULT_FROM_EMAIL,
        [payment_context['customer_email']],
        html_message=email_msg
    )


def send_verification_failure_mail(payment_context):
    email_msg = render_to_string('donation/verification_failure_mail.html', Context(payment_context))
    send_mail(
        'Donation verification failed!', None,
        settings.DEFAULT_FROM_EMAIL,
        settings.DONATE_EMAIL_RECIPIENTS,
        html_message=email_msg
    )
