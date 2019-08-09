from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from wagtail.wagtailcore.models import Site

from search.views import site_search
from .models import Resource, Room, Subject, Rack
from core.mixins import Page1Redirector


def build_resource_list_context(request_obj):
    return {
        'site': Site.find_for_request(request_obj),
        'tab': 'resources',
        'rooms': Room.objects.all().iterator(),
        'subjects': Subject.objects.all().iterator(),
        'current_page': 'resource-list'
    }


class ResourceList(Page1Redirector, ListView):
    paginate_by = 48
    context_object_name = "resources"
    model = Resource

    def get_queryset(self, *args, **kwargs):
        qs = super(ResourceList, self).get_queryset(*args, **kwargs).filter(live=True)
        return qs.order_by('-first_published_at')

    def get_context_data(self, **kwargs):
        context = super(ResourceList, self).get_context_data(**kwargs)
        context.update(build_resource_list_context(self.request))
        return context


def search_resources(request):
    search_context = site_search(request, only_return_context=True)
    search_context.update(build_resource_list_context(request))
    return render(request, 'resources/search_results.html', search_context)


class TaggedResourceList(ResourceList):
    def get_context_data(self, **kwargs):
        context = super(TaggedResourceList, self).get_context_data(**kwargs)
        context['site'] = Site.find_for_request(self.request)
        context['tag'] = self.kwargs['tag']
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(TaggedResourceList, self).get_queryset(*args, **kwargs)
        return qs.filter(tags__name__iexact=self.kwargs['tag'])


class RoomResourceList(ResourceList):
    def get_queryset(self):
        if not Room.objects.filter(slug=self.kwargs['slug']).exists():
            raise Http404
        qs = super(RoomResourceList, self).get_queryset()
        return qs.filter(rooms__slug=self.kwargs['slug'])


class RackResourceList(ResourceList):
    def get_queryset(self):
        if not Rack.objects.filter(slug=self.kwargs['rack_slug'],
                                   room__slug=self.kwargs['room_slug']).exists():
            raise Http404
        qs = super(RackResourceList, self).get_queryset()
        return qs.filter(racks__slug=self.kwargs['rack_slug'],
                         rooms__slug=self.kwargs['room_slug'])


class ResourceListBySubject(ResourceList):
    def get_queryset(self):
        qs = super(ResourceListBySubject, self).get_queryset()
        return qs.filter(subjects__slug=self.kwargs['slug'])


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
        context['site'] = Site.find_for_request(self.request)
        context['heading'] = 'no'
        context['tab'] = 'resources'
        for data in context['resource'].content:
            if data.block_type == 'factoids':
                context['heading'] = 'yes'
        context['current_page'] = 'resource-detail'
        return context
