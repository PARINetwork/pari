# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0012_auto_20190909_0930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rack',
            options={'ordering': ('room', 'name')},
        ),
        migrations.AlterField(
            model_name='resource',
            name='racks',
            field=modelcluster.fields.ParentalManyToManyField(related_name='resources', to='resources.Rack', blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='rooms',
            field=modelcluster.fields.ParentalManyToManyField(related_name='resources', to='resources.Room', blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='subjects',
            field=modelcluster.fields.ParentalManyToManyField(related_name='resources', to='resources.Subject', blank=True),
        ),
    ]
