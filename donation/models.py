from django.db import models

from core.mixins import TimestampedModel

from .helpers import DonationOptions


class RazorpayPlans(TimestampedModel):
    plan_name = models.CharField(max_length=16)
    amount = models.PositiveIntegerField()
    frequency = models.CharField(
        choices=DonationOptions.Frequency.MODEL_CHOICES,
        max_length=16
    )
    plan_id = models.CharField(
        max_length=64
    )

    class Meta:
        unique_together = (('amount', 'frequency'),)
        verbose_name_plural = 'Razorpay Plans'

    def __str__(self):
        return self.plan_name
