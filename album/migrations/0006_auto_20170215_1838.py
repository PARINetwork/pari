# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def add_location_to_album_image(apps, schema_editor):
    Album = apps.get_model('album.album')
    Image = apps.get_model('core.AffixImage')
    for album in Album.objects.all():
        location = album.locations.first()
        image_ids = album.slides.all().values_list('image_id', flat=True)
        for image_id in image_ids:
            image = Image.objects.get(id=image_id)
            image.locations.add(location)
            image.save()

class Migration(migrations.Migration):

    dependencies = [
        ('album', '0005_auto_20170124_1531'),
    ]

    operations = [
        migrations.RunPython(add_location_to_album_image),
    ]
