from django.views.generic import TemplateView
from django.contrib.contenttypes.models import ContentType

from wagtail.wagtailcore.models import Page


class PariNewsView(TemplateView):
    template_name = "news/pari_news.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PariNewsView, self).get_context_data(*args, **kwargs)
        page_content_type = ContentType.objects.get_for_model(Page)
        qs = Page.objects.live().exclude(content_type=page_content_type).order_by('-first_published_at')[:10]
        context['new_pages'] = qs
        return context
