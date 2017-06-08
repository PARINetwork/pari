# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20170124_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='show_featured_image',
            field=models.BooleanField(default=True),
        ),
    ]
