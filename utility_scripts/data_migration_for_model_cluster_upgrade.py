import json

from wagtail.wagtailcore.models import Page


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
            print "Updating a page-revision of page with ID: %-4s type: %-15s" % (
                revision.page.id, revision.page.content_type)
            revision.save()


if __name__ == '__main__':
    for page in Page.objects.all():
        for revision_ in page.revisions.all():
            update_m2m_fields(revision_)
