# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0002_auto_20190416_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='razorpayplans',
            name='frequency',
            field=models.CharField(max_length=16, choices=[('Monthly', 'Monthly'), ('Yearly', 'Yearly')]),
        ),
    ]
