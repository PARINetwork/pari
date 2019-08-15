# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv, re, urllib, logging

from django.db import migrations
from django.utils.text import slugify


logger = logging.getLogger(__file__)


def assign_resources_to_rooms_and_racks(apps, schema_editor):
    Resource = apps.get_model('resources', 'Resource')
    Room = apps.get_model('resources', 'Room')
    Rack = apps.get_model('resources', 'Rack')

    room_cache = {}
    rack_cache = {}

    with open('resources/migrations/data/resources_rooms_racks.csv', 'r') as csv_file:
        data = csv.reader(csv_file)
        _ = next(data, None)  # Skip header
        for row in data:
            room_name, rack_name, url = row[0].strip().title(), \
                                        row[1].strip().title(), \
                                        row[3].strip()

            if url:
                decoded_url = urllib.unquote(url).decode('utf-8')
            else:
                logger.error('Blank URL field. Skipping line >> %s <<' % ','.join(row))
                continue

            resource_slug = re.findall(r'.+/(.+)/$', decoded_url, re.UNICODE)[0]

            try:
                resource = Resource.objects.get(slug=resource_slug)
            except Resource.DoesNotExist:
                logger.error('Resource with slug %s not found. Skipping' % resource_slug)
                continue

            if room_cache.get(room_name):
                room = room_cache[room_name]
            else:
                try:
                    room = Room.objects.get(name=room_name)
                except Room.DoesNotExist:
                    room = Room.objects.create(name=room_name, slug=slugify(room_name))
                    logger.info('Created new room %s' % room_name)
                room_cache[room_name] = room

            room.resources.add(resource)

            if rack_name:
                rack_key = room_name + '/' + rack_name
                if rack_cache.get(rack_key):
                    rack = rack_cache[rack_key]
                else:
                    try:
                        rack = Rack.objects.get(name=rack_name, room=room)
                    except Rack.DoesNotExist:
                        rack = Rack.objects.create(name=rack_name, slug=slugify(rack_name), room=room)
                        logger.info('Created new rack %s' % rack_name)
                    rack_cache[rack_key] = rack

                rack.resources.add(resource)


def reverse_this_migration(apps, schema_editor):
    Resource = apps.get_model('resources', 'Resource')
    for resource in Resource.objects.all().iterator():
        resource.rooms.clear()
        resource.racks.clear()
    Room = apps.get_model('resources', 'Room')
    Room.objects.all().delete()
    Rack = apps.get_model('resources', 'Rack')
    Rack.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0009_auto_20190729_1053'),
    ]

    operations = [
        migrations.RunPython(assign_resources_to_rooms_and_racks, reverse_code=reverse_this_migration),
    ]
