from django.shortcuts import render
from django.http import Http404
from django.contrib.messages import success
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.vary import vary_on_headers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.forms import SearchForm

from .models import HomePage, StaticPage
from category.models import Category
from .forms import ContactForm


def home_page(request, slug="home-page"):
    home_page = HomePage.objects.get(slug=slug)
    return render(request, "core/home_page.html", {
        "page": home_page,
        "categories": Category.objects.all()[:9]
    })

def static_page(request, slug=None):
    try:
        page = Page.objects.get(slug=slug)
    except Page.DoesNotExist:
        raise Http404
    if page.specific_class == HomePage:
        return home_page(request, page.slug)
    return render(request, "core/static_page.html", {
        "self": page.specific
    })

def contribute(request, slug=None):
    page = StaticPage.objects.get(slug=slug)
    return render(request, "core/contribute.html", {
        "self": page
    })

def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success(request, _("Your query has successfully been sent"))
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, "core/contact_us.html", {
        "contact_form": form
    })


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
def search(request):
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
