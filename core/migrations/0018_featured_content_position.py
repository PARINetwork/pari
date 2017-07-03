# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import core.models
import wagtail.wagtailimages.blocks
import wagtail.wagtailimages.models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_making_title_and_link-text_non_mandatory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='featured_content',
            field=wagtail.wagtailcore.fields.StreamField([('featured_section', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'link_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock()), (b'position_from_left', core.models.IntegerBlock(default=10, max_value=75, required=True)), (b'position_from_top', core.models.IntegerBlock(default=20, max_value=40, required=True)), (b'featured_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'featured_image_label', wagtail.wagtailcore.blocks.CharBlock(required=False))]))], null=True, blank=True),
        ),
    ]
