# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields
import wagtail.core.blocks
import wagtail.images.blocks
import wagtail.images.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20170505_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='featured_content',
            field=wagtail.core.fields.StreamField([('featured_section', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=False)), (b'link_text', wagtail.core.blocks.CharBlock(required=False)), (b'url', wagtail.core.blocks.CharBlock()), (b'featured_image', wagtail.images.blocks.ImageChooserBlock()), (b'featured_image_label', wagtail.core.blocks.CharBlock(required=False))]))], null=True, blank=True),
        ),
    ]
