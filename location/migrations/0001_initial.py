# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('block', models.CharField(max_length=100, null=True, blank=True)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=set([('name', 'district', 'state')]),
        ),
    ]
