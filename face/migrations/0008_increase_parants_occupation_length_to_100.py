# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0007_increase_occupation_and_adivasi_max_length_to_100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face',
            name='occupation_of_parent',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
