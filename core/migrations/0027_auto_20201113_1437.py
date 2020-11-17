# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20201113_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guidelinespage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('heading_title', wagtail.wagtailcore.blocks.CharBlock()), ('heading_content', wagtail.wagtailcore.blocks.RichTextBlock()), ('sub_section_with_heading', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock()), ('content', wagtail.wagtailcore.blocks.RichTextBlock())))), ('sub_section_without_heading', wagtail.wagtailcore.blocks.RichTextBlock())), blank=True),
        ),
        migrations.AlterField(
            model_name='guidelinespage',
            name='language',
            field=models.CharField(max_length=7, choices=[('en', 'English'), ('as', 'Assamese'), ('bn', 'Bengali'), ('gu', 'Gujarati'), ('hi', 'Hindi'), ('kn', 'Kannada'), ('ml', 'Malayalam'), ('mr', 'Marathi'), ('lus', 'Mizo'), ('or', 'Odia'), ('pa', 'Punjabi'), ('te', 'Telugu'), ('ta', 'Tamil'), ('ur', 'Urdu')], default='English'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='featured_content',
            field=wagtail.wagtailcore.fields.StreamField((('featured_section', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock()), ('position_from_left', wagtail.wagtailcore.blocks.IntegerBlock(help_text='Value in percentage (Max: 75)', min_value=0, max_value=75, required=True, default=9)), ('position_from_top', wagtail.wagtailcore.blocks.IntegerBlock(help_text='Value in percentage (Max: 40)', min_value=0, max_value=40, required=True, default=30)), ('featured_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('featured_image_label', wagtail.wagtailcore.blocks.CharBlock(required=False))))),), null=True, blank=True),
        ),
    ]
