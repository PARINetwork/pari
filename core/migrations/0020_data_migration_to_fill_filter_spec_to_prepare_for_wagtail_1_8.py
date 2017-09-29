# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from wagtail.wagtailimages.utils import get_fill_filter_spec_migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_wagtail_1_7_changes_to_custom_image_and_rendition_classes'),
    ]

    forward, reverse = get_fill_filter_spec_migrations('core', 'AffixImageRendition')

    operations = [
        migrations.RunPython(forward, reverse),
    ]
