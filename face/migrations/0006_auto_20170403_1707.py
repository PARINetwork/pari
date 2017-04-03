# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0005_auto_20170303_1748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='face',
            old_name='description',
            new_name='additional_info',
        ),
        migrations.AddField(
            model_name='face',
            name='occupation_of_parent',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='face',
            name='occupation',
            field=models.CharField(help_text='Enter the occupation of the person', max_length=50, null=True, blank=True),
        ),
    ]
