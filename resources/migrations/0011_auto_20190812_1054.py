# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0010_auto_20190808_1610'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ('id',)},
        ),
        migrations.AddField(
            model_name='resource',
            name='show_day',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='show_month',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='show_year',
            field=models.BooleanField(default=True),
        ),
    ]
