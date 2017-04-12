# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0006_auto_20170403_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face',
            name='adivasi',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='face',
            name='occupation',
            field=models.CharField(help_text='Enter the occupation of the person', max_length=100, null=True, blank=True),
        ),
    ]
