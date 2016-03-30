import calendar
from bs4 import BeautifulSoup

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.sites.requests import RequestSite
from django.utils import translation
from django.conf import settings
from django.http import Http404
from django.core.cache import caches

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

    def render_to_response(self, context, **kwargs):
        response = super(ArticleDetail, self).render_to_response(context, **kwargs)
        if self.request.user.is_staff or self.request.GET.get("preview"):
            return response
        cache = caches['default']
        if cache.get(context['object'].get_absolute_url()):
            return cache.get(context['object'].get_absolute_url())
        content = response.rendered_content
        bs = BeautifulSoup(content, "html5lib")
        imgs = bs.find("div", class_="article-content").find_all("img")
        for img in imgs:
            if not img.attrs:
                continue
            if img.attrs.get("class") and "lazy" in img.attrs["class"]:
                continue
            img.attrs["data-original"] = img.attrs.get("src")
            img.attrs["class"] = img.attrs.get("class", []) + ["lazy"]
            img.attrs.pop("src")
        content = unicode(bs)
        response.content = content
        cache.set(context['object'].get_absolute_url(), response)
        return response


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
            live_articles_by_author = Article.objects.live().filter(
                authors__slug=self.kwargs["slug"]
            )
            qs = live_articles_by_author.order_by("-first_published_at")
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
