# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_author_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='bio_as',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='bio_bn',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='bio_en',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='bio_gu',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='bio_hi',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='bio_kn',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='bio_ml',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='bio_mr',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='bio_or',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='bio_pa',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='bio_ta',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='bio_te',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='bio_ur',
            field=models.TextField(null=True, blank=True),
        ),
    ]
