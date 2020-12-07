# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.images.models
import wagtail.core.fields
import wagtail.core.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('core', '0008_auto_20170220_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuidelinesPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page', on_delete=django.db.models.deletion.PROTECT)),
                ('types_of_articles', wagtail.core.fields.StreamField([('sub_section', wagtail.core.blocks.StructBlock([(b'heading', wagtail.core.blocks.CharBlock()), (b'content', wagtail.core.blocks.RichTextBlock(required=True))]))])),
                ('essential_writing_requirements', wagtail.core.fields.StreamField([('sub_section', wagtail.core.blocks.StructBlock([(b'heading', wagtail.core.blocks.CharBlock()), (b'content', wagtail.core.blocks.RichTextBlock(required=True))]))])),
                ('writing_tips', wagtail.core.fields.StreamField([('sub_section', wagtail.core.blocks.RichTextBlock(required=True))])),
                ('mailing_tips', wagtail.core.fields.StreamField([('sub_section', wagtail.core.blocks.RichTextBlock(required=True))])),
                ('photo_guidelines', wagtail.core.fields.StreamField([('sub_section', wagtail.core.blocks.RichTextBlock(required=True))])),
                ('video_guidelines', wagtail.core.fields.StreamField([('sub_section', wagtail.core.blocks.StructBlock([(b'heading', wagtail.core.blocks.CharBlock()), (b'content', wagtail.core.blocks.RichTextBlock(required=True))]))])),
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
