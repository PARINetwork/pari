# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_make_categories_non_mandatory'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
