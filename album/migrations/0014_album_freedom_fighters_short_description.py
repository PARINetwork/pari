# Generated by Django 2.2 on 2022-08-12 09:24

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0013_album_is_freedom_fighters_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='freedom_fighters_short_description',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]