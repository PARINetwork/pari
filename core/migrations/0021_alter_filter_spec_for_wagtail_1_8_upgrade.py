# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.images.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_data_migration_to_fill_filter_spec_to_prepare_for_wagtail_1_8'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiximagerendition',
            name='filter_spec',
            field=models.CharField(max_length=255, db_index=True),
        ),
        migrations.AlterField(
            model_name='affiximagerendition',
            name='focal_point_key',
            field=models.CharField(default='', max_length=16, editable=False, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='affiximagerendition',
            unique_together=set([('image', 'filter_spec', 'focal_point_key')]),
        ),
    ]
