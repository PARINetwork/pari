from __future__ import print_function
import gc
import json

from wagtail.core.models import PageRevision


def update_m2m_fields(revision):
    content_dict = json.loads(revision.content_json)
    m2m_fields = ['authors', 'translators', 'categories', 'locations']
    for m2m_field in m2m_fields:
        if m2m_field in content_dict and content_dict[m2m_field] and isinstance(content_dict[m2m_field][0], dict):
            pks = []
            for entity in content_dict[m2m_field]:
                pks.append(entity['pk'])
            content_dict[m2m_field] = pks
            revision.content_json = json.dumps(content_dict)
            print("Updating a page-revision of page with ID: %-4s type: %-15s" % (
                revision.page.id, revision.page.content_type))
            revision.save()


def batch_qs(qs, batch_size=200):
    total = qs.count()
    for start in range(0, total, batch_size):
        end = min(start + batch_size, total)
        yield qs[start:end]


if __name__ == '__main__':
    qs = PageRevision.objects.all().order_by('pk')
    for revision_qs in batch_qs(qs):
        revisions = list(revision_qs)
        for revision_ in revisions:
            update_m2m_fields(revision_)
        gc.collect()
