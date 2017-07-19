# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import face.models
import wagtail.wagtailimages.blocks
import article.streamfields.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_article_modular_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='modular_content',
            field=wagtail.wagtailcore.fields.StreamField([('full_width_image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.CharBlock(required=False))]))])), ('two_column_image', wagtail.wagtailcore.blocks.StructBlock([(b'image_left', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'image_right', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.CharBlock(required=False))]))])), ('paragraph', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock())])), ('paragraph_with_image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'align_image', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'left', choices=[(b'left', b'Left'), (b'right', b'Right')])), (b'content', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock())]))])), ('face', wagtail.wagtailcore.blocks.StructBlock([(b'face', article.streamfields.blocks.PageTypeChooserBlock(for_models=[face.models.Face]))])), ('paragraph_with_block_quote', wagtail.wagtailcore.blocks.StructBlock([(b'quote', wagtail.wagtailcore.blocks.RichTextBlock(editor=b'tinymce')), (b'align_quote', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'left', choices=[(b'left', b'Left'), (b'right', b'Right')])), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock())]))], null=True, blank=True),
        ),
    ]
