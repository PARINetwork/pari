# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_location_non_mandatory'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='show_day',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='article',
            name='show_month',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='article',
            name='show_year',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='show_featured_image',
            field=models.BooleanField(default=True),
        ),
    ]
