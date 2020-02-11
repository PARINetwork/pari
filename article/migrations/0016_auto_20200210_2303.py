# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_auto_20200210_2251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articleauthors',
            options={'ordering': ('sort_order',)},
        ),
        migrations.AddField(
            model_name='articleauthors',
            name='sort_order',
            field=models.IntegerField(default=0),
        ),
    ]
