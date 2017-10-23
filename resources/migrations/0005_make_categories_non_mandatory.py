# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_auto_20170124_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(related_name='resources_by_category', to='category.Category', blank=True),
        ),
    ]
