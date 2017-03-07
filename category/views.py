from django.conf import settings
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404

from category.models import Category
from article.models import Article


class CategoriesList(ListView):
    context_object_name = "categories"
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoriesList, self).get_context_data(**kwargs)
        context["tab"] = 'stories'
        return context


class GalleryDetail(DetailView):
    context_object_name = "category"
    model = Category
    paginate_by = 12

    # def get_absolute_url(self):
    #     return reverse("gallery-detail", kwargs={"slug": self.slug})
    def get_context_data(self, **kwargs):

        category_title = {'VideoZone': 'Videos',
                          'AudioZone': 'Audios'}
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
        context["title"] = category_title.get(category_name, category_name)
        context["tab"] = 'gallery'
        return context

class StoryDetail(DetailView):
    context_object_name = "category"
    model = Category
    paginate_by = 12

    # def get_absolute_url(self):
    #     return reverse("gallery-detail", kwargs={"slug": self.slug})
    def get_context_data(self, **kwargs):

        category_title = {'VideoZone': 'Videos',
                          'AudioZone': 'Audios'}
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
        context["title"] = category_title.get(category_name, category_name)
        context["tab"] = 'stories'
        return context
