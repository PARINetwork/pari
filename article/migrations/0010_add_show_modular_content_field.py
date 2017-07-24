# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_add_stream_fields_for_modular_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='show_modular_content',
            field=models.BooleanField(default=False),
        ),
    ]
