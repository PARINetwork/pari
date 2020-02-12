# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):
    dependencies = [
        ('author', '0005_auto_20170124_1609'),
        ('article', '0014_auto_20190416_1659'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name='ArticleAuthors',
                    fields=[
                        ('id',
                         models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                    ],
                    options={
                        'db_table': 'article_article_authors',
                    },
                ),
                migrations.RemoveField(
                    model_name='article',
                    name='authors',
                ),
                migrations.AddField(
                    model_name='articleauthors',
                    name='article',
                    field=modelcluster.fields.ParentalKey(related_name='authors', to='article.Article'),
                ),
                migrations.AddField(
                    model_name='articleauthors',
                    name='author',
                    field=models.ForeignKey(related_name='articles_by_author', to='author.Author'),
                ),
                migrations.AlterUniqueTogether(
                    name='articleauthors',
                    unique_together=set([('article', 'author')]),
                ),
            ]
        )
    ]
