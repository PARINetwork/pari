# Generated by Django 2.2 on 2022-08-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0012_auto_20220512_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='is_freedom_fighters_album',
            field=models.BooleanField(default=False),
        ),
    ]