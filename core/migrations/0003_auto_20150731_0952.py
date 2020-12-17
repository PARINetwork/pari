# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.images.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150730_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='language',
            field=models.CharField(max_length=7, choices=[(b'bn', 'Bengali'), (b'en', 'English'), (b'hi', 'Hindi'), (b'ka', 'Kannada'), (b'ml', 'Malayalam'), (b'mr', 'Marathi'), (b'or', 'Oriya'), (b'te', 'Telugu'), (b'ta', 'Tamil')]),
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='language',
            field=models.CharField(max_length=7, choices=[(b'bn', 'Bengali'), (b'en', 'English'), (b'hi', 'Hindi'), (b'ka', 'Kannada'), (b'ml', 'Malayalam'), (b'mr', 'Marathi'), (b'or', 'Oriya'), (b'te', 'Telugu'), (b'ta', 'Tamil')]),
        ),
    ]
