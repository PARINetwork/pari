# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.images.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20201113_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guidelinespage',
            name='content',
            field=wagtail.core.fields.StreamField((('heading_title', wagtail.core.blocks.CharBlock()), ('heading_content', wagtail.core.blocks.RichTextBlock()), ('sub_section_with_heading', wagtail.core.blocks.StructBlock((('heading', wagtail.core.blocks.CharBlock()), ('content', wagtail.core.blocks.RichTextBlock())))), ('sub_section_without_heading', wagtail.core.blocks.RichTextBlock())), blank=True),
        ),
        migrations.AlterField(
            model_name='guidelinespage',
            name='language',
            field=models.CharField(max_length=7, choices=[('en', 'English'), ('as', 'Assamese'), ('bn', 'Bengali'), ('gu', 'Gujarati'), ('hi', 'Hindi'), ('kn', 'Kannada'), ('ml', 'Malayalam'), ('mr', 'Marathi'), ('lus', 'Mizo'), ('or', 'Odia'), ('pa', 'Punjabi'), ('te', 'Telugu'), ('ta', 'Tamil'), ('ur', 'Urdu')], default='English'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='featured_content',
            field=wagtail.core.fields.StreamField((('featured_section', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(required=False)), ('url', wagtail.core.blocks.CharBlock()), ('position_from_left', wagtail.core.blocks.IntegerBlock(help_text='Value in percentage (Max: 75)', min_value=0, max_value=75, required=True, default=9)), ('position_from_top', wagtail.core.blocks.IntegerBlock(help_text='Value in percentage (Max: 40)', min_value=0, max_value=40, required=True, default=30)), ('featured_image', wagtail.images.blocks.ImageChooserBlock()), ('featured_image_label', wagtail.core.blocks.CharBlock(required=False))))),), null=True, blank=True),
        ),
    ]
