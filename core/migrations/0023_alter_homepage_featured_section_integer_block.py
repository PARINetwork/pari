# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailimages.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_remove_filter_field_for_wagtail_1_9_upgrade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='featured_content',
            field=wagtail.wagtailcore.fields.StreamField([('featured_section', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock()), (b'position_from_left', wagtail.wagtailcore.blocks.IntegerBlock(help_text='Value in percentage (Max: 75)', max_value=75, default=9, min_value=0, required=True)), (b'position_from_top', wagtail.wagtailcore.blocks.IntegerBlock(help_text='Value in percentage (Max: 40)', max_value=40, default=30, min_value=0, required=True)), (b'featured_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'featured_image_label', wagtail.wagtailcore.blocks.CharBlock(required=False))]))], null=True, blank=True),
        ),
    ]
