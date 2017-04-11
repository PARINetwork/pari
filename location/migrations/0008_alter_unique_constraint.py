# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0007_add_panchayat_and_alter_subdistrict_fields'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=set([('name', 'district', 'state', 'panchayat', 'sub_district_name')]),
        ),
    ]
