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


class DonorInfo(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=13, blank=False)
    pan = models.CharField(max_length=10, blank=False)
    address = models.TextField(max_length=252, blank=False)
    payment_method = models.CharField(max_length=100, blank=False)
    donation_date_time = models.DateTimeField(blank=False)
    is_indian = models.BooleanField(default=False)

    class Meta:
        db_table = 'donation_donor_info'

    def __str__(self):
        return self.pan
