# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.images.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_add_field_carousel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiximage',
            name='file',
            field=models.ImageField(height_field='height', upload_to=wagtail.images.models.get_upload_to, width_field='width', verbose_name='file'),
        ),
        migrations.AlterField(
            model_name='affiximagerendition',
            name='file',
            field=models.ImageField(height_field='height', width_field='width', upload_to=wagtail.images.models.get_rendition_upload_to),
        ),
    ]
