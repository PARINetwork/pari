# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailimages.models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0009_remove_album_photographers'),
        ('wagtailcore', '0028_merge'),
        ('article', '0005_auto_20170124_1531'),
        ('core', '0011_auto_20170412_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='about',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='announcements',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='strap',
        ),
        migrations.AddField(
            model_name='homepage',
            name='featured_content',
            field=wagtail.wagtailcore.fields.StreamField([('featured_section', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock()), (b'link_title', wagtail.wagtailcore.blocks.CharBlock()), (b'featured_page', wagtail.wagtailcore.blocks.PageChooserBlock())]))], null=True, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='in_focus_link',
            field=models.TextField(null=True, verbose_name='Link', blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='in_focus_link_text',
            field=models.TextField(null=True, verbose_name='Link Text', blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='in_focus_page1',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, verbose_name='Page one', blank=True, to='wagtailcore.Page', null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='in_focus_page2',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, verbose_name='Page two', blank=True, to='wagtailcore.Page', null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='in_focus_title',
            field=models.TextField(null=True, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='photo_album',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, blank=True, to='album.Album', null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='talking_album',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, blank=True, to='album.Album', null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='article.Article', null=True),
        ),
    ]
