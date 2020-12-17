# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import core.apps


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0008_auto_20190429_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', core.apps.ModelSlugField(help_text='Auto-populated field. Edit manually only if you must', max_length=255)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='ResourceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('slug', core.apps.ModelSlugField(help_text='Auto-populated field. Edit manually only if you must', unique=True, max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('slug', core.apps.ModelSlugField(help_text='Auto-populated field. Edit manually only if you must', unique=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='rack',
            name='room',
            field=models.ForeignKey(related_name='racks', to='resources.Room', on_delete=django.db.models.deletion.CASCADE),
        ),
        migrations.AddField(
            model_name='resource',
            name='racks',
            field=modelcluster.fields.ParentalManyToManyField(related_name='resources', to='resources.Rack'),
        ),
        migrations.AddField(
            model_name='resource',
            name='rooms',
            field=modelcluster.fields.ParentalManyToManyField(related_name='resources', to='resources.Room'),
        ),
        migrations.AddField(
            model_name='resource',
            name='subjects',
            field=modelcluster.fields.ParentalManyToManyField(related_name='resources', to='resources.Subject', blank=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='type',
            field=models.ForeignKey(related_name='resources', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='resources.ResourceType', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='rack',
            unique_together=set([('name', 'room'), ('slug', 'room')]),
        ),
    ]
