# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.db import migrations


def transform_page_revision_authors(apps, schema_editor):
    PageRevision = apps.get_model('wagtailcore', 'PageRevision')
    Article = apps.get_model('article', 'Article')
    ArticleAuthors = apps.get_model('article', 'ArticleAuthors')
    articles = Article.objects.all().iterator()
    page_ids = [x.pk for x in articles]
    page_revisions = PageRevision.objects.filter(page_id__in=page_ids).iterator()
    for page_rev in page_revisions:
        content_json = json.loads(page_rev.content_json)
        author_ids = content_json['authors']
        new_authors = []
        for author_id in author_ids:
            try:
                article_author_id = ArticleAuthors.objects.get(article_id=page_rev.page_id, author_id=author_id).pk
            except ArticleAuthors.DoesNotExist:
                article_author_id = None
            new_authors.append({
                'pk': article_author_id,
                'sort_order': 0,
                'author': author_id,
                'article': page_rev.page_id
            })
        content_json['authors'] = new_authors
        page_rev.content_json = json.dumps(content_json)
        page_rev.save()


def undo_transform(apps, schema_editor):
    PageRevision = apps.get_model('wagtailcore', 'PageRevision')
    Article = apps.get_model('article', 'Article')
    articles = Article.objects.all().iterator()
    page_ids = [x.pk for x in articles]
    page_revisions = PageRevision.objects.filter(page_id__in=page_ids).iterator()
    for page_rev in page_revisions:
        content_json = json.loads(page_rev.content_json)
        author_dicts = content_json['authors']
        old_authors = [author_dict['author'] for author_dict in author_dicts]
        content_json['authors'] = old_authors
        page_rev.content_json = json.dumps(content_json)
        page_rev.save()


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_auto_20200210_2303'),
    ]

    operations = [
        migrations.RunPython(transform_page_revision_authors, undo_transform),
    ]
