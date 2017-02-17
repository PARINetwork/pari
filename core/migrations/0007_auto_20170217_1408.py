# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailimages.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20170124_1531'),
    ]

    operations = [
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
