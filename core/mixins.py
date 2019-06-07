from django.core.paginator import InvalidPage
from django.db import models
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView


class TimestampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class ListViewWithCustomPagination(ListView):
    def paginate_queryset(self, queryset, page_size):
        paginator = self.get_paginator(queryset, page_size, allow_empty_first_page=self.get_allow_empty())
        page = self.kwargs.get('page') or self.request.GET.get('page') or 1
        try:
            page_number = int(page)
        except ValueError:
            if page == 'last':
                page_number = paginator.num_pages
            else:
                raise Http404(_(u"Page is not 'last', nor can it be converted to an int."))
        try:
            page = paginator.page(page_number)
        except InvalidPage:
            # page = paginator.page(paginator.num_pages)
            page = paginator.page(1)

        return paginator, page, page.object_list, page.has_other_pages()
