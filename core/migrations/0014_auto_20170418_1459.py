# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields
import wagtail.core.blocks
import wagtail.images.blocks
import wagtail.images.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20170418_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='featured_content',
            field=wagtail.core.fields.StreamField([('featured_section', wagtail.core.blocks.StructBlock([(b'title', wagtail.core.blocks.CharBlock()), (b'link_text', wagtail.core.blocks.CharBlock()), (b'url', wagtail.core.blocks.CharBlock()), (b'featured_image', wagtail.images.blocks.ImageChooserBlock())]))], null=True, blank=True),
        ),
    ]
