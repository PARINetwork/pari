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
        filteredList = ['videozone', 'audiozone', 'faces', 'photozone']
        context['filtered_categories']=[]
        for category in context['categories']:
            if category.slug not in filteredList:
                context['filtered_categories'].append(category)
        context['current_page'] = 'categories-list'
        return context


class GalleryDetail(DetailView):
    context_object_name = "category"
    model = Category
    paginate_by = 12
    template_name = 'category/gallery_detail.html'

    # def get_absolute_url(self):
    #     return reverse("gallery-detail", kwargs={"slug": self.slug})
    def get_context_data(self, **kwargs):

        category_heading_options = {'VideoZone': {'title': 'Videos', 'sub_heading': 'stories told in moving pictures'},
                                    'AudioZone': {'title': 'Audios', 'sub_heading': 'you could listen all day'}}
        context = super(GalleryDetail, self).get_context_data(**kwargs)
        qs = Article.objects.live().select_related('featured_image')
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
        category = context["category"]
        context["title"] = category_heading_options.get(category.name, {'title': category.name}).get('title')
        context["sub_heading"] = category_heading_options.get(category.name,
                                                              {'sub_heading': category.description}).get('sub_heading')
        context["tab"] = 'gallery'

        categories_in_gallery = ['Little takes', 'tongues', 'visible-work-invisible-women']
        if context["category"].slug in categories_in_gallery:
            self.template_name = 'category/category_detail.html'
        context['current_page'] = category.name
        return context


class StoryDetail(DetailView):
    context_object_name = "category"
    model = Category
    paginate_by = 12

    # def get_absolute_url(self):
    #     return reverse("gallery-detail", kwargs={"slug": self.slug})
    def get_context_data(self, **kwargs):
        context = super(StoryDetail, self).get_context_data(**kwargs)
        qs = Article.objects.live().select_related('featured_image')
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
        category = context['category']
        context["title"] = category.name
        context["sub_heading"] = category.description
        context["tab"] = 'stories'
        context["current_page"] = 'single-category'
        return context


def gallery_home_page(request, slug=None):
    albums = Album.objects.live()
    articles = Article.objects.live()
    album_details = get_album_and_photographers(albums)
    video = get_video(articles)
    talking_album = album_details['talking_album'][0]
    photo_album = album_details['photo_album'][0]
    gallery_context = {
        'talking_album': {
            'image': talking_album.slides.first().image,
            'photographers': album_details['talking_album'][1],
            'section_model': talking_album,
        },
        'photo_album': {
            'image': photo_album.slides.first().image,
            'photographers': album_details['photo_album'][1],
            'section_model': photo_album,
        },
        'video': {
            'image': video.featured_image,
            'photographers': video.authors.all(),
            'section_model': video,
        },
        'tab': 'gallery',
        'current_page': 'gallery-home',
    }
    return render(request, "category/gallery_home_page.html", gallery_context)


def get_album_and_photographers(albums):
    talking_album = None
    photo_album = None
    for album in albums:
        if len(album.slides.first().audio) > 0: #talking album has audio
            talking_album = album
            if photo_album is not None:
                break
        else:
            photo_album = album
            if talking_album is not None:
                break
    talking_album_photographers = get_unique_photographers(talking_album)
    photo_album_photographers = get_unique_photographers(photo_album)
    album_details = {}
    album_details['talking_album'] = [talking_album, talking_album_photographers]
    album_details['photo_album'] = [photo_album, photo_album_photographers]

    return album_details


def get_unique_photographers(talking_album):
    photographers = []
    for slide in talking_album.slides.all():
        photographers.extend(slide.image.photographers.all())
    return set(photographers)


def get_video(articles):
    for article in articles:
        if article.categories.filter(name='VideoZone'):
            return article
    return None
