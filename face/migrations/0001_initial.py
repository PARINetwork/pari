# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.core.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '__first__'),
        ('core', '0001_initial'),
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Face',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page', on_delete=django.db.models.deletion.PROTECT)),
                ('description', wagtail.core.fields.RichTextField(default='<p><strong>Occupation:</strong></p>\n<p><strong>Village:</strong></p>\n<p><strong>Block:</strong></p>\n<p><strong>District:</strong></p>\n<p><strong>State:</strong></p>\n<p><strong>Region:</strong></p>\n<p><strong>Date:</strong></p>\n<p><strong>Photographer:</strong></p>\n', blank=True)),
                ('image', models.ForeignKey(related_name='face_for_image', on_delete=django.db.models.deletion.SET_NULL, to='core.AffixImage', null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='location.Location', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
