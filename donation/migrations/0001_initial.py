# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RazorpayPlans',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('plan_name', models.CharField(max_length=16)),
                ('amount', models.PositiveIntegerField()),
                ('frequency', models.CharField(max_length=16, choices=[(b'Monthly', b'Monthly'), (b'Yearly', b'Yearly')])),
                ('plan_id', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='razorpayplans',
            unique_together=set([('amount', 'frequency')]),
        ),
    ]
