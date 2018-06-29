# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20180629_1241'),
        ('face', '0008_increase_parants_occupation_length_to_100'),
    ]

    operations = [
        migrations.AddField(
            model_name='face',
            name='original_image',
            field=models.ForeignKey(related_name='original_image', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='core.AffixImage', null=True),
        ),
    ]
