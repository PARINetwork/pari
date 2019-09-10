# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0011_auto_20190812_1054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rack',
            options={'ordering': ('room__name', 'name')},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='resource',
            name='racks',
            field=models.ManyToManyField(related_name='resources', to='resources.Rack', blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='rooms',
            field=models.ManyToManyField(related_name='resources', to='resources.Room', blank=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='subjects',
            field=models.ManyToManyField(related_name='resources', to='resources.Subject', blank=True),
        ),
    ]
