# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields
import wagtail.core.blocks
import face.models
import wagtail.images.blocks
import article.streamfields.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_made_date_fields_selectable'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='modular_content',
            field=wagtail.core.fields.StreamField([('full_width_image', wagtail.core.blocks.StructBlock([(b'image', wagtail.core.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock()), (b'caption', wagtail.core.blocks.CharBlock(required=False))]))])), ('two_column_image', wagtail.core.blocks.StructBlock([(b'image_left', wagtail.core.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock()), (b'caption', wagtail.core.blocks.CharBlock(required=False))])), (b'image_right', wagtail.core.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock()), (b'caption', wagtail.core.blocks.CharBlock(required=False))]))])), ('paragraph', wagtail.core.blocks.StructBlock([(b'content', wagtail.core.blocks.RichTextBlock())])), ('paragraph_with_image', wagtail.core.blocks.StructBlock([(b'image', wagtail.core.blocks.StructBlock([(b'image', wagtail.images.blocks.ImageChooserBlock()), (b'caption', wagtail.core.blocks.CharBlock(required=False))])), (b'align_image', wagtail.core.blocks.ChoiceBlock(default=b'left', choices=[(b'left', b'Left'), (b'right', b'Right')])), (b'content', wagtail.core.blocks.StructBlock([(b'content', wagtail.core.blocks.RichTextBlock())]))])), ('face', wagtail.core.blocks.StructBlock([(b'face', article.streamfields.blocks.PageTypeChooserBlock(for_models=[face.models.Face]))])), ('paragraph_with_block_quote', wagtail.core.blocks.StructBlock([(b'quote', article.streamfields.blocks.RichTextMiniBlock()), (b'align_quote', wagtail.core.blocks.ChoiceBlock(default=b'right', choices=[(b'left', b'Left'), (b'right', b'Right')])), (b'paragraph', wagtail.core.blocks.RichTextBlock())]))], null=True, blank=True),
        ),
    ]
