from __future__ import absolute_import, unicode_literals

import urllib

from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.vary import vary_on_headers
from wagtail.admin.forms.search import SearchForm
from wagtail.core import models
from wagtail.core.models import Page
from wagtail.search.backends import get_search_backend
from wagtail.search.models import Query

from author.models import Author
from location.models import Location

SITE_SEARCH_OPERATOR = 'and'


def site_search(
        request,
        template=None,
        template_ajax=None,
        results_per_page=10,
        use_json=False,
        json_attrs=['title', 'url'],
        show_unpublished=False,
        search_title_only=False,
        extra_filters={},
        path=None,
        only_return_context=False):
    # Get default templates
    if template is None:
        if hasattr(settings, 'WAGTAILSEARCH_RESULTS_TEMPLATE'):
            template = settings.WAGTAILSEARCH_RESULTS_TEMPLATE
        else:
            template = 'wagtailsearch/search_results.html'

    if template_ajax is None:
        if hasattr(settings, 'WAGTAILSEARCH_RESULTS_TEMPLATE_AJAX'):
            template_ajax = settings.WAGTAILSEARCH_RESULTS_TEMPLATE_AJAX
        else:
            template_ajax = template

    # Get query string and page from GET paramters
    query_string = request.GET.get('q', '')
    page = request.GET.get('page', request.GET.get('p', 1))
    type_filters = request.GET.getlist('type')
    category_filters = request.GET.getlist('category')
    language_filters = request.GET.getlist('language')
    start_date = request.GET.get('start-date')
    end_date = request.GET.get('end-date')
    sort_by = request.GET.get('sort-by')
    location_filters = request.GET.getlist('location')
    author_filters = request.GET.getlist('author')

    raw_filters = []
    index_prefixes = ['album_album', 'article_article', 'resources_resource', 'face_face', 'core_staticpage']

    def build_raw_filters_for_index(index_name, filters):
        return list(map(lambda prefix: {
            "terms": {
                prefix + '__' + index_name: filters
            }
        }, index_prefixes))

    # Search
    if query_string != '':
        es_backend = get_search_backend()

        pages = models.Page.objects.filter(path__startswith=(path or request.site.root_page.path))

        if not show_unpublished:
            pages = pages.live()

        if extra_filters:
            pages = pages.filter(**extra_filters)

        if type_filters:
            raw_type_filters = build_raw_filters_for_index('get_search_type_filter', type_filters)
            raw_filters.append({"bool": {"should": raw_type_filters}})

        if category_filters:
            raw_category_filters = build_raw_filters_for_index('get_categories_filter', category_filters)
            raw_filters.append({"bool": {"should": raw_category_filters}})

        if language_filters:
            raw_language_filters = build_raw_filters_for_index('language_filter', language_filters)
            raw_filters.append({"bool": {"should": raw_language_filters}})

        if location_filters:
            raw_location_filters = build_raw_filters_for_index('get_minimal_locations_filter', location_filters)
            raw_filters.append({"bool": {"should": raw_location_filters}})

        if author_filters:
            raw_author_filters = build_raw_filters_for_index('get_authors_or_photographers_filter', author_filters)
            raw_filters.append({"bool": {"should": raw_author_filters}})

        if start_date:
            pages = pages.filter(first_published_at__range=(start_date, end_date or timezone.now()))

        if search_title_only:
            search_results = pages.search(query_string, fields=['title'], operator=SITE_SEARCH_OPERATOR)
        elif sort_by == 'latest':
            pages = pages.order_by('-first_published_at')
            search_results = es_backend.search(query_string, pages, order_by_relevance=False,
                                               operator=SITE_SEARCH_OPERATOR,
                                               extra_raw_filters=raw_filters)
        else:
            search_results = es_backend.search(query_string, pages, operator=SITE_SEARCH_OPERATOR,
                                               extra_raw_filters=raw_filters)

        # Get query object
        query = Query.get(query_string)

        # Add hit
        query.add_hit()

        # Pagination
        paginator = Paginator(search_results, results_per_page)
        try:
            search_results = paginator.page(page)
        except PageNotAnInteger:
            search_results = paginator.page(1)
        except EmptyPage:
            search_results = paginator.page(paginator.num_pages)
    else:
        query = None
        search_results = None

    if use_json:
        # Return a json response
        if search_results:
            search_results_json = []
            for result in search_results:
                result_specific = result.specific

                search_results_json.append(dict(
                    (attr, getattr(result_specific, attr))
                    for attr in json_attrs
                    if hasattr(result_specific, attr)
                ))

            return JsonResponse(search_results_json, safe=False)
        else:
            return JsonResponse([], safe=False)
    else:
        # Render a template
        if request.is_ajax() and template_ajax:
            template = template_ajax

        query_params_string = ''.join(
            ['&q=%s' % query if query else ''] +
            ['&type=%s' % _ for _ in type_filters] +
            ['&category=%s' % _ for _ in category_filters] +
            ['&language=%s' % _ for _ in language_filters] +
            ['&start-date=%s' % start_date if start_date else ''] +
            ['&end-date=%s' % end_date if end_date else ''] +
            ['&location=%s' % _ for _ in location_filters] +
            ['&sort-by=%s' % sort_by if sort_by else '']
        )
        if author_filters:
            for author in author_filters:
                query_params_string += '&author=' + urllib.parse.quote_plus(author)

        locations = set(location.district + ', ' + location.state for location in Location.objects.all())

        authors = set(str(author) for author in Author.objects.all())

        context_obj = dict(
            query_string=query_string,
            languages=settings.LANGUAGES,
            search_results=search_results,
            is_ajax=request.is_ajax(),
            query=query,
            locations=locations,
            authors=authors,
            query_params_string=query_params_string
        )

        if only_return_context:
            return context_obj

        return render(request, template, context_obj)


# TODO: Remove the below two functions when we migrate to wagtail 1.2

DEFAULT_PAGE_KEY = 'p'


def paginate(request, items, page_key=DEFAULT_PAGE_KEY, per_page=20):
    page = request.GET.get(page_key, 1)

    paginator = Paginator(items, per_page)
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return paginator, page


@vary_on_headers('X-Requested-With')
def admin_search(request):
    pages = []
    q = None

    if 'q' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']

            pages = Page.objects.all().prefetch_related('content_type').search(q)
            paginator, pages = paginate(request, pages)
    else:
        form = SearchForm()

    if request.is_ajax():
        return render(request, "wagtailadmin/pages/search_results.html", {
            'pages': pages,
            'query_string': q,
            'pagination_query_params': ('q=%s' % q) if q else ''
        })
    else:
        return render(request, "wagtailadmin/pages/search.html", {
            'search_form': form,
            'pages': pages,
            'query_string': q,
            'pagination_query_params': ('q=%s' % q) if q else ''
        })
