# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailimages.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_20170704_featured_content_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiximagerendition',
            name='filter_spec',
            field=models.CharField(default='', max_length=255, db_index=True, blank=True),
        ),
        migrations.AlterField(
            model_name='affiximagerendition',
            name='filter',
            field=models.ForeignKey(related_name='+', blank=True, to='wagtailimages.Filter', null=True),
        ),
    ]
