# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailimages.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20170217_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='affiximage',
            name='photographer',
        ),
    ]
