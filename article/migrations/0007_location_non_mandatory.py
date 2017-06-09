# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_article_show_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='locations',
            field=modelcluster.fields.M2MField(related_name='articles_by_location', to='location.Location', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='show_featured_image',
            field=models.BooleanField(default=True, help_text='Hide for One-off video'),
        ),
    ]
