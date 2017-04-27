# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.text import slugify


def compute_slug(location):
    return slugify("%s-%s" % (location.id, location.name))[:50]


class Migration(migrations.Migration):
    def update_slug(apps, schema_editor):
        Location = apps.get_model('location.location')
        for location in Location.objects.all():
            location.slug = compute_slug(location)
            location.save()

    dependencies = [
        ('location', '0008_alter_unique_constraint'),
    ]

    operations = [
        migrations.RunPython(update_slug),
    ]
