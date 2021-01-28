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

    class Term(object):
        M6 = '6 Months'
        Y1 = '1 Year'
        Y2 = '2 Years'
        Y3 = '3 Years'
        Y5 = '5 Years'
        Y10 = '10 Years'
        CHOICES = (
            (M6, M6),
            (Y1, Y1),
            (Y2, Y2),
            (Y3, Y3),
            (Y5, Y5),
            (Y10, Y10),
        )

        @classmethod
        def get_num_periods(cls, frequency, term):
            if frequency == DonationOptions.Frequency.M:
                return 6 if term == cls.M6 else int(term[:2].rstrip()) * 12
            elif frequency == DonationOptions.Frequency.Y:
                if term == cls.M6 or term == cls.Y1:
                    raise ValueError('Term should be at least 2 years for Yearly recurrence')
                else:
                    return int(term[:2].rstrip())


def send_acknowledgement_mail(payment_context):
    email_msg = render_to_string('donation/acknowledgement_mail.html', payment_context)
    send_mail(
        'We have received your donation', None,
        settings.DEFAULT_FROM_EMAIL,
        [payment_context['customer_email']],
        html_message=email_msg
    )


def send_verification_failure_mail(payment_context):
    email_msg = render_to_string('donation/verification_failure_mail.html', payment_context)
    send_mail(
        'Donation verification failed!', None,
        settings.DEFAULT_FROM_EMAIL,
        settings.DONATE_EMAIL_RECIPIENTS,
        html_message=email_msg
    )
