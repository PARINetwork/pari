# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailimages.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_alter_filter_spec_for_wagtail_1_8_upgrade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='affiximagerendition',
            name='filter',
        ),
    ]
