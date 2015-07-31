# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='language',
            field=models.CharField(max_length=7, choices=[(b'bn', 'Bengali'), (b'en', 'English'), (b'hi', 'Hindi'), (b'ka', 'Kannada'), (b'ml', 'Malayalam'), (b'mr', 'Marathi'), (b'or', 'Oriya'), (b'te', 'Telugu'), (b'ta', 'Tamil')]),
        ),
    ]
