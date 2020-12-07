# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0005_auto_20170303_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='block',
        ),
        migrations.RemoveField(
            model_name='location',
            name='mandapam',
        ),
        migrations.RemoveField(
            model_name='location',
            name='others',
        ),
        migrations.RemoveField(
            model_name='location',
            name='sub_district',
        ),
        migrations.RemoveField(
            model_name='location',
            name='taluka',
        ),
        migrations.RemoveField(
            model_name='location',
            name='tehsil',
        ),
        migrations.AlterField(
            model_name='location',
            name='sub_district_type',
            field=models.ForeignKey(related_name='location', blank=True, to='location.SubDistrictType', null=True, on_delete=django.db.models.deletion.CASCADE),
        ),
    ]
