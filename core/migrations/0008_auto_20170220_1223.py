# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.images.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20170217_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='affiximage',
            name='photographer',
        ),
        migrations.AddField(
            model_name='affiximage',
            name='camera',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='affiximage',
            name='date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
