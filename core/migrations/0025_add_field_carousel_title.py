# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailimages.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_language_field_for_guidelines_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='carousel_title',
            field=models.TextField(default='Latest On PARI'),
        ),
    ]
