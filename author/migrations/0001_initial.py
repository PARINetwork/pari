# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('slug', models.SlugField()),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('twitter_username', models.CharField(max_length=50, null=True, blank=True)),
                ('facebook_username', models.CharField(max_length=50, null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('image', models.ForeignKey(blank=True, to='core.AffixImage', null=True, on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
