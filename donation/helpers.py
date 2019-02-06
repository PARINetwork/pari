# -*- coding: utf-8 -*-


class DonationOptions(object):
    class Amount(object):
        Rs500 = '500'
        Rs1000 = '1000'
        Rs2000 = '2000'
        CHOICES = (
            (Rs500,  u'₹ 500'),
            (Rs1000, u'₹ 1000'),
            (Rs2000, u'₹ 2000'),
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
