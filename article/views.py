import calendar
from bs4 import BeautifulSoup
from django.views.generic import ListView

from django.views.generic.detail import DetailView
from django.conf import settings
from django.http import Http404
from django.core.cache import caches
from django.contrib.contenttypes.models import ContentType

from wagtail.core.models import Page

from article.models import Article
from author.models import Author
from core.utils import get_translations_for_page, filter_by_language

from album.models import Album
from face.models import Face
from resources.models import Resource
from core.mixins import Page1Redirector


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
        arc = ContentType.objects.get_for_model(Article)
        alc = ContentType.objects.get_for_model(Album)
        fac = ContentType.objects.get_for_model(Face)
        rec = ContentType.objects.get_for_model(Resource)
        context['new_list'] = Page.objects.live()\
                                          .filter(content_type__in=[
                                              arc, alc, fac, rec
                                          ])\
                                          .order_by('-first_published_at')[:4]
        context['MAP_KEY'] = settings.GOOGLE_MAP_KEY
        context['current_page'] = 'article-detail'
        context['beginning_authors_with_role'] = self.object.beginning_authors_with_role()
        context['end_authors_with_role'] = self.object.end_authors_with_role()
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
            ns_attrs = img.attrs
            ns_img = bs.new_tag("img", **ns_attrs)
            img.insert_before(ns_img)
            ns_img.wrap(bs.new_tag("noscript"))
            if img.attrs.get("class") and "lazyload" in img.attrs["class"]:
                continue
            img.attrs["class"] = img.attrs.get("class", []) + ["lazyload"]
            if img.attrs.get("src"):
                img.attrs["data-src"] = img.attrs.get("src")
            if img.attrs.get("srcset"):
                img.attrs["data-srcset"] = img.attrs.get("srcset")
                img.attrs.pop("srcset", "")
            gray_gif = "data:image/gif;base64,R0lGODlhAQABAIAAAMLCwgAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw=="
            img.attrs["src"] = gray_gif
        content = bs.decode('utf-8','ignore')
        response.content = content
        cache.set(context['object'].get_absolute_url(), response)
        return response


class ArchiveDetail(Page1Redirector, ListView):
    context_object_name = "articles"
    model = Article
    template_name = 'article/archive_article_list.html'
    paginate_by = 12

    def get_queryset(self):
        year = self.kwargs['year']
        month = self.kwargs['month']
        qs = Article.objects.live().filter(first_published_at__year=year,
                                      first_published_at__month=month).order_by('-first_published_at')
        qs, = filter_by_language(self.request, qs)
        return qs

    def get_context_data(self, **kwargs):
        context = super(ArchiveDetail, self).get_context_data(**kwargs)
        context['year'] = self.kwargs["year"]
        context['month'] = self.kwargs["month"]
        context['month_as_name'] = calendar.month_name[int(context["month"])]
        context['title'] = "{0} {1}".format(context['month_as_name'], context["year"])
        context['LANGAUAGES'] = settings.LANGUAGES
        context['current_page'] = 'archive-detail'
        return context


class AuthorArticleList(Page1Redirector, ListView):
    context_object_name = "articles"
    paginate_by = 12
    template_name = "article/author_article_list.html"

    def get_queryset(self):
        live_articles_by_author = Article.objects.live().filter(
            authors__author__slug=self.kwargs["slug"]
        )
        qs = live_articles_by_author.order_by("-first_published_at")
        qs, = filter_by_language(self.request, qs)
        return qs

    def get_context_data(self, **kwargs):
        context = super(AuthorArticleList, self).get_context_data(**kwargs)
        try:
            author = Author.objects.get(slug=self.kwargs["slug"])
        except Author.DoesNotExist:
            raise Http404
        context["authors"] = [author]
        context["title"] = "All stories by %s" %(author.name)
        context["articles"] = context["page_obj"]
        context['LANGUAGES'] = settings.LANGUAGES
        context['current_page'] = 'author-detail'
        return context


class ArticleList(Page1Redirector, ListView):
    context_object_name = "articles"
    model = Article
    paginate_by = 12
    template_name = 'article/archive_article_list.html'

    def get_queryset(self):
        url_name = self.request.resolver_match.url_name
        if url_name == "author-detail":
            live_articles_by_author = Article.objects.live().filter(
                authors__author__slug=self.kwargs["slug"]
            )
            qs = live_articles_by_author.order_by("-first_published_at")
        else:
            qs = super(ArticleList, self).get_queryset().filter(live=True)
        if self.request.GET.get("lang"):
            qs = qs.filter(language=self.request.GET["lang"])
        return qs

    def get_context_data(self, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        current_page_type = self.kwargs['filter']
        url_name = self.request.resolver_match.url_name
        context['title'] = "All articles"
        if url_name == "author-detail":
            try:
                context["author"] = Author.objects.get(slug=self.kwargs["slug"])
            except Author.DoesNotExist:
                raise Http404
            context["title"] = context["author"].name
        context["articles"] = context["page_obj"]
        context['LANGUAGES'] = settings.LANGUAGES
        context['current_page'] = current_page_type
        return context


class GalleryArticleList(Page1Redirector, ListView):
    context_object_name = "articles"
    model = Article
    paginate_by = 12
    template_name = 'includes/gallery_article_list.html'

    def get_queryset(self):
        url_name = self.request.resolver_match.url_name
        if url_name == "author-detail":
            live_articles_by_author = Article.objects.live().filter(
                authors__slug=self.kwargs["slug"]
            )
            qs = live_articles_by_author.order_by("-first_published_at")
        else:
            qs = super(GalleryArticleList, self).get_queryset()
        if self.request.GET.get("lang"):
            qs = qs.filter(language=self.request.GET["lang"])
        return qs

    def get_context_data(self, **kwargs):
        context = super(GalleryArticleList, self).get_context_data(**kwargs)
        url_name = self.request.resolver_match.url_name
        context['title'] = "All articles"
        if url_name == "author-detail":
            try:
                context["author"] = Author.objects.get(slug=self.kwargs["slug"])
            except Author.DoesNotExist:
                raise Http404
            context["title"] = context["author"].name
        context["articles"] = context["page_obj"]
        context['LANGUAGES'] = settings.LANGUAGES
        context['current_page'] = 'gallery-article-list'
        return context


class TaggedArticleList(ArticleList):
    def get_queryset(self):
        qs = super(TaggedArticleList, self).get_queryset()
        qs = qs.filter(tags__name__iexact=self.kwargs['tag'])
        return qs

    def get_context_data(self, **kwargs):
        context = super(TaggedArticleList, self).get_context_data(**kwargs)
        context['title'] = "All articles tagged \"%s\"" %(self.kwargs['tag'])
        return context
