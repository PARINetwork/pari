# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='face',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('as', 'Assamese'), ('bn', 'Bengali'), ('gu', 'Gujarati'), ('hi', 'Hindi'), ('kn', 'Kannada'), ('ml', 'Malayalam'), ('mr', 'Marathi'), ('or', 'Odia'), ('pa', 'Punjabi'), ('te', 'Telugu'), ('ta', 'Tamil'), ('ur', 'Urdu')], default='en', max_length=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='face',
            name='description',
            field=wagtail.core.fields.RichTextField(blank=True, default='<p><strong>Occupation:</strong> </p>\n<p><strong>Village:</strong> </p>\n<p><strong>Block:</strong> </p>\n<p><strong>District:</strong> </p>\n<p><strong>State:</strong> </p>\n<p><strong>Region:</strong> </p>\n<p><strong>Date:</strong> &lt;Month:String&gt; &lt;Date:Number&gt;, &lt;Year:Number&gt;</p>\n<p><strong>Photographer:</strong> </p>\n<p><strong>Camera:</strong> </p>\n'),
        ),
    ]
