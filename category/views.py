from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from article.models import Article
from category.models import Category
from core.mixins import Page1Redirector
from core.models import GalleryHomePage
from core.utils import filter_by_language, get_translations_for_articles, get_unique_photographers


class CategoriesList(ListView):
    context_object_name = "categories"
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoriesList, self).get_context_data(**kwargs)
        context["tab"] = 'stories'
        context["gallery"] = ['audiozone', 'Little takes',
                              'tongues', 'visible-work-invisible-women',
                              'photozone', 'videozone']
        filteredList = ['videozone', 'audiozone', 'faces', 'photozone']
        context['filtered_categories']=[]
        for category in context['categories']:
            if category.slug not in filteredList:
                context['filtered_categories'].append(category)
        context['current_page'] = 'categories-list'
        return context


class GalleryDetail(Page1Redirector, DetailView):
    context_object_name = "category"
    model = Category
    paginate_by = 12
    template_name = 'category/gallery_detail.html'

    # def get_absolute_url(self):
    #     return reverse("gallery-detail", kwargs={"slug": self.slug})
    def get_context_data(self, **kwargs):
        context = super(GalleryDetail, self).get_context_data(**kwargs)
        qs = Article.objects.live().select_related('featured_image')
        qs = qs.filter(categories=context["category"])
        qs, = filter_by_language(self.request, qs)
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
        category = context["category"]
        context["title"] = category.name
        context["sub_heading"] = category.description
        context["tab"] = 'gallery'

        categories_in_gallery = ['Little takes', 'tongues', 'visible-work-invisible-women']
        if context["category"].slug in categories_in_gallery:
            self.template_name = 'category/category_detail.html'
        context['current_page'] = category.name
        return context


class StoryDetail(Page1Redirector, DetailView):
    context_object_name = "category"
    model = Category
    paginate_by = 12

    # def get_absolute_url(self):
    #     return reverse("gallery-detail", kwargs={"slug": self.slug})
    def get_context_data(self, **kwargs):
        context = super(StoryDetail, self).get_context_data(**kwargs)
        qs = Article.objects.live().select_related('featured_image')
        qs = qs.filter(categories=context["category"])
        qs, = filter_by_language(self.request, qs)
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
        category = context['category']
        context["title"] = category.name
        context["sub_heading"] = category.description
        context["tab"] = 'stories'
        context["current_page"] = 'single-category'
        return context


def gallery_home_page(request, slug="gallery"):
    gallery_page = GalleryHomePage.objects.get(slug=slug)
    video = gallery_page.video
    talking_album = gallery_page.talking_album
    photo_album = gallery_page.photo_album
    gallery_context = {
        'talking_album': {
            'image': talking_album.slides.first().image,
            'photographers': get_unique_photographers(talking_album),
            'section_model': talking_album,
        },
        'photo_album': {
            'image': photo_album.slides.first().image,
            'photographers': get_unique_photographers(photo_album),
            'section_model': photo_album,
        },
        'video': {
            'image': video.featured_image,
            'photographers': video.authors.all(),
            'section_model': video,
        },
        'page': gallery_page,
        'tab': 'gallery',
        'current_page': 'gallery-home',
    }
    return render(request, "category/gallery_home_page.html", gallery_context)