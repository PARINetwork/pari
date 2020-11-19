# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_alter_content_and_modular_content_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=wagtail.core.fields.RichTextField(verbose_name="Content - Deprecated. Use 'MODULAR CONTENT' instead.", blank=True),
        ),
    ]
