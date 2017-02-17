# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    def add_photographers_to_album_image(apps, schema_editor):
        Album = apps.get_model('album.album')
        Image = apps.get_model('core.AffixImage')
        for album in Album.objects.all():
            photographers = album.photographers.all()
            image_ids = album.slides.all().values_list('image_id', flat=True)
            for image_id in image_ids:
                image = Image.objects.get(id=image_id)
                image.photographers.add(*photographers)
                image.save()

    dependencies = [
        ('album', '0007_remove_album_locations'),
        ('core', '0007_auto_20170217_1247'),
    ]

    operations = [
        migrations.RunPython(add_photographers_to_album_image),
    ]
