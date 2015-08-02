from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator

from category.models import Category
from article.models import Article


class CategoriesList(ListView):
    context_object_name = "categories"
    model = Category


class CategoryDetail(DetailView):
    context_object_name = "category"
    model = Category
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        qs = Article.objects.filter(categories=context["category"]).live()
        paginator = Paginator(qs, self.paginate_by)
        try:
            page_num = self.request.GET.get("page", 1)
        except ValueError:
            page_num = 1
        context["articles"] = paginator.page(page_num)
        return context
