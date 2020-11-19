# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import core.models
import wagtail.images.blocks
import wagtail.images.models
import wagtail.core.fields
import wagtail.core.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_making_title_and_link-text_non_mandatory'),
    ]

    operations = [
       
        migrations.AlterField(
            model_name='homepage',
            name='featured_content',
            field=wagtail.core.fields.StreamField([('featured_section', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock(required=False)), (b'link_text', wagtail.core.blocks.CharBlock(required=False)), (b'url', wagtail.core.blocks.CharBlock()), (b'position_from_left', core.models.IntegerBlock(help_text='Value in percentage (Max: 75)', max_value=75, default=9, required=True)), (b'position_from_top', core.models.IntegerBlock(help_text='Value in percentage (Max: 40)', max_value=40, default=30, required=True)), (b'featured_image', wagtail.images.blocks.ImageChooserBlock()), (b'featured_image_label', wagtail.core.blocks.CharBlock(required=False))]))], null=True, blank=True),
        ),
    ]