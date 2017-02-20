# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0008_auto_20170217_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='photographers',
        ),
    ]
