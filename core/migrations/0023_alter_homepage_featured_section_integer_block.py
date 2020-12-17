# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields
import wagtail.core.blocks
import wagtail.images.blocks
import wagtail.images.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_remove_filter_field_for_wagtail_1_9_upgrade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='featured_content',
            field=wagtail.core.fields.StreamField([('featured_section', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=False)), (b'link_text', wagtail.core.blocks.CharBlock(required=False)), (b'url', wagtail.core.blocks.CharBlock()), (b'position_from_left', wagtail.core.blocks.IntegerBlock(help_text='Value in percentage (Max: 75)', max_value=75, default=9, min_value=0, required=True)), (b'position_from_top', wagtail.core.blocks.IntegerBlock(help_text='Value in percentage (Max: 40)', max_value=40, default=30, min_value=0, required=True)), (b'featured_image', wagtail.images.blocks.ImageChooserBlock()), (b'featured_image_label', wagtail.core.blocks.CharBlock(required=False))]))], null=True, blank=True),
        ),
    ]
