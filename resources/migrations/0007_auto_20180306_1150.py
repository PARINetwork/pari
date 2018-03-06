# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0007_merge'),
        ('core', '0026_auto_20180306_1150'),
        ('resources', '0006_add_field_for_absolute_slideshare_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='absolute_url',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='embed_thumbnail',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='embed_url',
        ),
        migrations.AddField(
            model_name='resource',
            name='document',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtaildocs.Document', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='thumbnail',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='core.AffixImage', max_length=500, null=True),
        ),
    ]
