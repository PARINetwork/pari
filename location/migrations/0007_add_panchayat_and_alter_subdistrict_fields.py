# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_auto_20170303_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='sub_district_type_value',
            new_name='sub_district_name',
        ),
        migrations.AddField(
            model_name='location',
            name='panchayat',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
