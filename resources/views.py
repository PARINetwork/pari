from django.http import Http404
from django.views.generic import DetailView, ListView
from django.contrib.sites.requests import RequestSite

from .models import Resource


class ResourceList(ListView):
    paginate_by = 48
    context_object_name = "resources"
    model = Resource

    def get_queryset(self, *args, **kwargs):
        qs = super(ResourceList, self).get_queryset(*args, **kwargs).filter(live=True)
        return qs.order_by('-first_published_at')

    def get_context_data(self, **kwargs):
        context = super(ResourceList, self).get_context_data(**kwargs)
        context['tab'] = 'resources'
        context['current_page'] = 'resource-list'
        return context


class TaggedResourceList(ResourceList):
    def get_context_data(self, **kwargs):
        context = super(TaggedResourceList, self).get_context_data(**kwargs)
        context['tag'] = self.kwargs['tag']
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(TaggedResourceList, self).get_queryset(*args, **kwargs)
        return qs.filter(tags__name__iexact=self.kwargs['tag'])


class ResourceDetail(DetailView):
    context_object_name = "resource"
    model = Resource

    def get_object(self, queryset=None):
        obj = super(ResourceDetail, self).get_object(queryset)
        if self.request.GET.get("preview"):
            obj = obj.get_latest_revision_as_page()
            return obj
        if not obj.live:
            raise Http404
        return obj

    def get_context_data(self, **kwargs):
        context = super(ResourceDetail, self).get_context_data(**kwargs)
        context['site'] = RequestSite(self.request)
        context['heading'] = 'no'
        for data in context['resource'].content:
            if data.block_type == 'factoids':
                context['heading'] = 'yes'
        context['current_page'] = 'resource-detail'
        return context


class ReportDetail(DetailView):
    context_object_name = "resource"
    model = Resource
    template_name = 'resources/report_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ReportDetail, self).get_context_data(**kwargs)
        context['site'] = RequestSite(self.request)
        context['current_page'] = 'report-detail'
        return context
