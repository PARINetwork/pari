# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_auto_20160619_1946'),
        ('article', '0002_auto_20150731_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='translators',
            field=modelcluster.fields.ParentalManyToManyField(related_name='translations_by_author', to='author.Author', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='language',
            field=models.CharField(max_length=7, choices=[(b'en', 'English'), (b'as', 'Assamese'), (b'bn', 'Bengali'), (b'gu', 'Gujarati'), (b'hi', 'Hindi'), (b'kn', 'Kannada'), (b'ml', 'Malayalam'), (b'mr', 'Marathi'), (b'or', 'Odia'), (b'pa', 'Punjabi'), (b'te', 'Telugu'), (b'ta', 'Tamil'), (b'ur', 'Urdu')]),
        ),
    ]
