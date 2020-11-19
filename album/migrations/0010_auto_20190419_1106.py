# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('album', '0009_remove_album_photographers'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_object', modelcluster.fields.ParentalKey(related_name='tagged_items', to='album.Album')),
                ('tag', models.ForeignKey(related_name='album_albumtag_items', to='taggit.Tag', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='album',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(to='taggit.Tag', through='album.AlbumTag', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
