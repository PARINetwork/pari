# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_auto_20160619_1946'),
        ('album', '0002_auto_20150731_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='photographer',
        ),
        migrations.AddField(
            model_name='album',
            name='photographers',
            field=modelcluster.fields.M2MField(related_name='albums_by_photographer', to='author.Author', blank=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='language',
            field=models.CharField(max_length=7, choices=[(b'en', 'English'), (b'as', 'Assamese'), (b'bn', 'Bengali'), (b'gu', 'Gujarati'), (b'hi', 'Hindi'), (b'kn', 'Kannada'), (b'ml', 'Malayalam'), (b'mr', 'Marathi'), (b'or', 'Odia'), (b'pa', 'Punjabi'), (b'te', 'Telugu'), (b'ta', 'Tamil'), (b'ur', 'Urdu')]),
        ),
    ]
