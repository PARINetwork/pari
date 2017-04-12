# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailimages.models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0009_remove_album_photographers'),
        ('wagtailcore', '0028_merge'),
        ('article', '0005_auto_20170124_1531'),
        ('core', '0010_auto_20170330_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryHomePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('photo_title', models.TextField()),
                ('photo_link', models.TextField(null=True, blank=True)),
                ('photo_album', models.ForeignKey(related_name='photo', on_delete=django.db.models.deletion.PROTECT, to='album.Album')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='galleryhomepage',
            name='photo_of_the_week',
            field=models.ForeignKey(to='core.AffixImage', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='galleryhomepage',
            name='talking_album',
            field=models.ForeignKey(related_name='talking', on_delete=django.db.models.deletion.PROTECT, to='album.Album'),
        ),
        migrations.AddField(
            model_name='galleryhomepage',
            name='video',
            field=models.ForeignKey(to='article.Article', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
