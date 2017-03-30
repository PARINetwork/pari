# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailimages.models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20170328_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guidelinespage',
            name='essential_writing_requirements',
        ),
        migrations.RemoveField(
            model_name='guidelinespage',
            name='mailing_tips',
        ),
        migrations.RemoveField(
            model_name='guidelinespage',
            name='photo_guidelines',
        ),
        migrations.RemoveField(
            model_name='guidelinespage',
            name='types_of_articles',
        ),
        migrations.RemoveField(
            model_name='guidelinespage',
            name='video_guidelines',
        ),
        migrations.RemoveField(
            model_name='guidelinespage',
            name='writing_tips',
        ),
        migrations.AddField(
            model_name='guidelinespage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField([('heading_title', wagtail.wagtailcore.blocks.CharBlock()), ('heading_content', wagtail.wagtailcore.blocks.RichTextBlock()), ('sub_section_with_heading', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock()), (b'content', wagtail.wagtailcore.blocks.RichTextBlock())])), ('sub_section_without_heading', wagtail.wagtailcore.blocks.RichTextBlock())], blank=True),
        ),
        migrations.AddField(
            model_name='guidelinespage',
            name='strap',
            field=models.TextField(blank=True),
        ),
    ]
