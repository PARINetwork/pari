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
            model_name='homepage',
            name='carousel_title',
            field=models.TextField(default='Latest On PARI'),
        ),
    ]
