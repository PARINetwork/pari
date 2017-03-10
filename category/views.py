from django.conf import settings
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.shortcuts import render

from album.models import Album
from category.models import Category
from article.models import Article


class CategoriesList(ListView):
    context_object_name = "categories"
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoriesList, self).get_context_data(**kwargs)
        context["tab"] = 'stories'
        context["gallery"] = ['audiozone', 'Little takes',
                              'tongues', 'visible-work-invisible-women',
                              'photozone', 'videozone']
        return context


class GalleryDetail(DetailView):
    context_object_name = "category"
    model = Category
    paginate_by = 12

    # def get_absolute_url(self):
    #     return reverse("gallery-detail", kwargs={"slug": self.slug})
    def get_context_data(self, **kwargs):

        category_heading_options = {'VideoZone': {'title': 'Videos', 'sub_heading': 'stories told in moving pictures'},
                          'AudioZone': {'title': 'Audios', 'sub_heading': 'you could listen all day'}}
        context = super(GalleryDetail, self).get_context_data(**kwargs)
        qs = Article.objects.live()
        qs = qs.filter(categories=context["category"])
        if self.request.GET.get("lang"):
            qs = qs.filter(language=self.request.GET["lang"])
        qs = qs.order_by('-first_published_at')
        paginator = Paginator(qs, self.paginate_by)
        try:
            page_num = self.request.GET.get("page", 1)
        except ValueError:
            page_num = 1
        try:
            context["articles"] = paginator.page(page_num)
        except (PageNotAnInteger, EmptyPage):
            raise Http404
        context["languages"] = settings.LANGUAGES
        category_name = context["category"].name
        context["title"] = category_heading_options.get(category_name, {'title': category_name}).get('title')
        context["sub_heading"] = category_heading_options.get(category_name, {'sub_heading': ''}).get('sub_heading')
        context["tab"] = 'gallery'
        return context


class StoryDetail(DetailView):
    context_object_name = "category"
    model = Category
    paginate_by = 12

    # def get_absolute_url(self):
    #     return reverse("gallery-detail", kwargs={"slug": self.slug})
    def get_context_data(self, **kwargs):
        context = super(StoryDetail, self).get_context_data(**kwargs)
        qs = Article.objects.live()
        qs = qs.filter(categories=context["category"])
        if self.request.GET.get("lang"):
            qs = qs.filter(language=self.request.GET["lang"])
        qs = qs.order_by('-first_published_at')
        paginator = Paginator(qs, self.paginate_by)
        try:
            page_num = self.request.GET.get("page", 1)
        except ValueError:
            page_num = 1
        try:
            context["articles"] = paginator.page(page_num)
        except (PageNotAnInteger, EmptyPage):
            raise Http404
        context["languages"] = settings.LANGUAGES
        category_name = context["category"].name
        context["title"] = category_name
        context["tab"] = 'stories'
        return context


def gallery_home_page(request, slug=None):
    albums = Album.objects.live()
    articles = Article.objects.live()
    photographers, talking_album = get_album_and_photographers(albums)
    video = get_video(articles)

    return render(request, "category/gallery_home_page.html", {
        'talking_album': talking_album,
        'photographers': set(photographers),
        'video': video,
    })


def get_album_and_photographers(albums):
    talking_album = None
    for album in albums:
        if album.slides.first().audio is not '':
            talking_album = album
            break
    photographers = []
    for slide in album.slides.all():
        photographers.extend(slide.image.photographers.all())
    return photographers, talking_album


def get_video(articles):
    for article in articles:
        if article.categories.filter(name='VideoZone'):
            return article
    return None
