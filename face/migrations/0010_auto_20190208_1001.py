# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0009_face_original_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face',
            name='original_image',
            field=models.ForeignKey(related_name='original_image', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='core.AffixImage', null=True),
        ),
    ]
