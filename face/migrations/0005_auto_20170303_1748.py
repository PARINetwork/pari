# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0004_auto_20170217_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Place of Origin', to='location.Location', null=True),
        ),
        migrations.AlterField(
            model_name='face',
            name='occupation',
            field=models.CharField(help_text='Enter the occupation of the parent if this is the face of a child', max_length=50, null=True, blank=True),
        ),
    ]
