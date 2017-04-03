# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_auto_20170303_1624'),
    ]

    operations = [
        migrations.RunSQL(
            "INSERT INTO location_subdistricttype (name) VALUES ('block'), ('sub_district'), ('taluka'), ('tehsil'), ('mandapam'), ('mandal')")
    ]
