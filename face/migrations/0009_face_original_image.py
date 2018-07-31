# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0008_increase_parants_occupation_length_to_100'),
    ]

    operations = [
        migrations.AddField(
            model_name='face',
            name='original_image',
            field=models.ForeignKey(related_name='original_image', on_delete=django.db.models.deletion.SET_NULL, blank=True, max_length=500, to='core.AffixImage', null=True),
        ),
    ]
