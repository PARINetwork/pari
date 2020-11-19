# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20170217_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubDistrictType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='sub_district_type_value',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='sub_district_type',
            field=models.ForeignKey(related_name='locations', blank=True, to='location.SubDistrictType', null=True, on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
