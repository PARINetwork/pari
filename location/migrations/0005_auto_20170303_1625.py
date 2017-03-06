# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def move_subdistrict(apps, schema_editor):
    Location = apps.get_model('location.location')
    SubDistrictType = apps.get_model('location.subdistricttype')
    for location in Location.objects.all():
        sub_district_options = ['block', 'sub_district', 'taluka', 'tehsil', 'mandapam']
        for option in sub_district_options:
            if getattr(location, option) != None:
                filtered_sub_district_type = SubDistrictType.objects.filter(name=option)
                location.sub_district_type = filtered_sub_district_type[0]
                location.sub_district_type_value = getattr(location, option)
                location.save()
                break

class Migration(migrations.Migration):

    dependencies = [
        ('location', '0004_auto_20170303_1624'),
    ]

    operations = [
        migrations.RunPython(move_subdistrict),
    ]
