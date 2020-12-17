# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.images.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160521_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('as', 'Assamese'), ('bn', 'Bengali'), ('gu', 'Gujarati'), ('hi', 'Hindi'), ('kn', 'Kannada'), ('ml', 'Malayalam'), ('mr', 'Marathi'), ('or', 'Odia'), ('pa', 'Punjabi'), ('te', 'Telugu'), ('ta', 'Tamil'), ('ur', 'Urdu')], max_length=7),
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('as', 'Assamese'), ('bn', 'Bengali'), ('gu', 'Gujarati'), ('hi', 'Hindi'), ('kn', 'Kannada'), ('ml', 'Malayalam'), ('mr', 'Marathi'), ('or', 'Odia'), ('pa', 'Punjabi'), ('te', 'Telugu'), ('ta', 'Tamil'), ('ur', 'Urdu')], max_length=7),
        ),
    ]
