# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailimages.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_alter_homepage_featured_section_integer_block'),
    ]

    operations = [
        migrations.AddField(
            model_name='guidelinespage',
            name='language',
            field=models.CharField(default='English', max_length=7, choices=[(b'en', 'English'), (b'as', 'Assamese'), (b'bn', 'Bengali'), (b'gu', 'Gujarati'), (b'hi', 'Hindi'), (b'kn', 'Kannada'), (b'ml', 'Malayalam'), (b'mr', 'Marathi'), (b'lus', 'Mizo'), (b'or', 'Odia'), (b'pa', 'Punjabi'), (b'te', 'Telugu'), (b'ta', 'Tamil'), (b'ur', 'Urdu')]),
        ),
    ]
