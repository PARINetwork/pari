# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.images.models
from django.conf import settings
import django.db.models.deletion
import wagtail.core.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('core', '0003_auto_20150731_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiximage',
            name='collection',
            field=models.ForeignKey(related_name='+', default=wagtail.core.models.get_root_collection_id, verbose_name='collection', to='wagtailcore.Collection', on_delete=django.db.models.deletion.CASCADE),
        ),
        migrations.AlterField(
            model_name='affiximage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at', db_index=True),
        ),
        migrations.AlterField(
            model_name='affiximage',
            name='height',
            field=models.IntegerField(verbose_name='height', editable=False),
        ),
        migrations.AlterField(
            model_name='affiximage',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text=None, verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='affiximage',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='affiximage',
            name='uploaded_by_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='uploaded by user'),
        ),
        migrations.AlterField(
            model_name='affiximage',
            name='width',
            field=models.IntegerField(verbose_name='width', editable=False),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='language',
            field=models.CharField(max_length=7, choices=[(b'as', 'Assamese'), (b'bn', 'Bengali'), (b'en', 'English'), (b'hi', 'Hindi'), (b'ka', 'Kannada'), (b'ml', 'Malayalam'), (b'mr', 'Marathi'), (b'or', 'Oriya'), (b'te', 'Telugu'), (b'ta', 'Tamil'), (b'ur', 'Urdu')]),
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='language',
            field=models.CharField(max_length=7, choices=[(b'as', 'Assamese'), (b'bn', 'Bengali'), (b'en', 'English'), (b'hi', 'Hindi'), (b'ka', 'Kannada'), (b'ml', 'Malayalam'), (b'mr', 'Marathi'), (b'or', 'Oriya'), (b'te', 'Telugu'), (b'ta', 'Tamil'), (b'ur', 'Urdu')]),
        ),
    ]
