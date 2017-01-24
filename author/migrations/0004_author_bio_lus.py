# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_auto_20160619_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='bio_lus',
            field=models.TextField(null=True, blank=True),
        ),
    ]
