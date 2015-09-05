import calendar

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.sites.requests import RequestSite
from django.utils import translation
from django.conf import settings
from django.http import Http404

from article.models import Article
from author.models import Author
from core.utils import get_translations_for_page


class ArticleDetail(DetailView):
    template_name = "article/article.html"
    model = Article

    def get_object(self, queryset=None):
        obj = super(ArticleDetail, self).get_object(queryset)
        if self.request.user.is_staff or self.request.GET.get("preview"):
            obj = obj.get_latest_revision_as_page()
            return obj
        if not obj.live:
            raise Http404
        return obj

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        translations = get_translations_for_page(context['object'])
        context['translations'] = translations
        context['site'] = RequestSite(self.request)
        return context


class ArchiveDetail(ListView):
    context_object_name = "articles"
    model = Article
    template_name = 'article/article_list.html'
    paginate_by = 10

    def get_queryset(self):
        year = self.kwargs['year']
        month = self.kwargs['month']
        return Article.objects.live().filter(first_published_at__year=year,
                                             first_published_at__month=month)

    def get_context_data(self, **kwargs):
        context = super(ArchiveDetail, self).get_context_data(**kwargs)
        context['year'] = self.kwargs["year"]
        context['month'] = self.kwargs["month"]
        context['month_as_name'] = calendar.month_name[int(context["month"])]
        context['title'] = "{0} {1}".format(context['month_as_name'], context["year"])
        return context


class ArticleList(ListView):
    context_object_name = "articles"
    model = Article
    paginate_by = 10

    def get_queryset(self):
        url_name = self.request.resolver_match.url_name
        if url_name == "author-detail":
            qs = Article.objects.live().filter(authors__slug=self.kwargs["slug"])
        else:
            qs = super(ArticleList, self).get_queryset()
        return qs

    def get_context_data(self, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        url_name = self.request.resolver_match.url_name
        context['title'] = "All articles"
        if url_name == "author-detail":
            try:
                context["author"] = Author.objects.get(slug=self.kwargs["slug"])
            except Author.DoesNotExist:
                raise Http404
            context["title"] = context["author"].name
        context["articles"] = context["page_obj"]
        return context
