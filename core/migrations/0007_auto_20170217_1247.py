# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.images.models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0005_auto_20170124_1609'),
        ('core', '0006_auto_20170124_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiximage',
            name='photographers',
            field=models.ManyToManyField(related_name='images_of_photographer', to='author.Author', blank=True),
        ),
    ]
