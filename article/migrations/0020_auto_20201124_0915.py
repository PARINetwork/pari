# Generated by Django 2.2 on 2020-11-24 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0019_auto_20201113_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='page_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page'),
        ),
        migrations.AlterField(
            model_name='articletag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_articletag_items', to='taggit.Tag'),
        ),
    ]
