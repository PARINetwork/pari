# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0017_auto_20200211_0038'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='articleauthors',
            unique_together=set([('article', 'author', 'sort_order')]),
        ),
    ]
