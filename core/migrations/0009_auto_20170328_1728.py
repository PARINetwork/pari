# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailimages.models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('core', '0008_auto_20170220_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuidelinesPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('types_of_articles', wagtail.wagtailcore.fields.StreamField([('sub_section', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock()), (b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=True))]))])),
                ('essential_writing_requirements', wagtail.wagtailcore.fields.StreamField([('sub_section', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock()), (b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=True))]))])),
                ('writing_tips', wagtail.wagtailcore.fields.StreamField([('sub_section', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])),
                ('mailing_tips', wagtail.wagtailcore.fields.StreamField([('sub_section', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])),
                ('photo_guidelines', wagtail.wagtailcore.fields.StreamField([('sub_section', wagtail.wagtailcore.blocks.RichTextBlock(required=True))])),
                ('video_guidelines', wagtail.wagtailcore.fields.StreamField([('sub_section', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock()), (b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=True))]))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='affiximage',
            name='date',
            field=models.DateTimeField(null=True, verbose_name='captured date', blank=True),
        )
    ]
