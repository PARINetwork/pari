# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0003_auto_20170124_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='face',
            name='adivasi',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='face',
            name='age',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='face',
            name='child',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='face',
            name='gender',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[('F', 'Female'), ('M', 'Male'), ('T', 'Transgender')]),
        ),
        migrations.AddField(
            model_name='face',
            name='occupation',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='face',
            name='quote',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='face',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
