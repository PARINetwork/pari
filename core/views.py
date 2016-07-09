import hmac
import json
import urllib
import hashlib

from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.messages import success
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.vary import vary_on_headers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from wagtail.wagtailcore.models import Page, Site
from wagtail.wagtailadmin.forms import SearchForm

from .models import HomePage, StaticPage
from category.models import Category
from .forms import ContactForm, DonateForm

from core.utils import get_translations_for_page


def home_page(request, slug="home-page"):
    home_page = HomePage.objects.get(slug=slug)
    translations = get_translations_for_page(home_page)
    return render(request, "core/home_page.html", {
        "page": home_page,
        "categories": Category.objects.all(),
        "translations": translations
    })

def static_page(request, slug=None):
    try:
        page = Page.objects.get(slug=slug)
    except Page.DoesNotExist:
        raise Http404
    if page.specific_class == HomePage:
        return home_page(request, page.slug)
    translations = get_translations_for_page(page.specific)
    return render(request, "core/static_page.html", {
        "self": page.specific,
        "translations": translations
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


def donate_form(request):
    form = DonateForm()
    errors = None
    try:
        site = Site.objects.get(hostname=request.get_host())
    except Site.DoesNotExist:
        site = Site.objects.filter(is_default_site=True)[0]
    if request.method == "POST":
        form = DonateForm(request.POST)
        if form.is_valid():
            pg_url = settings.INSTAMOJO["DONATE_URL"]
            params = {
                "data_name": form.cleaned_data["name"],
                "data_email": form.cleaned_data["email"],
                "data_phone": form.cleaned_data["phone"],
                "data_Field_90444": form.cleaned_data["pan"],
            }
            pg_url += "?{0}".format(urllib.urlencode(params))
            return HttpResponseRedirect(pg_url)
    return render(request, 'core/donate_form.html', {
        "form": form,
        "errors": errors,
        "site": site,
    })


def donate_success(request):
    try:
        site = Site.objects.get(hostname=request.get_host())
    except Site.DoesNotExist:
        site = Site.objects.filter(is_default_site=True)[0]
    return render(request, 'core/donate_success.html', {
        "site": site,
    })


def lower_first_item(item):
    return item[0].lower()


@csrf_exempt
@require_POST
def donate_webhook(request):
    status = 400
    data = request.POST.copy()
    hook_mac = data.pop("mac", [None])[0]
    keys = sorted(data.items(), key=lower_first_item)
    vals = "|".join([ii[1] for ii in keys])
    calc_mac = hmac.new(
        settings.INSTAMOJO["SALT"],
        vals,
        hashlib.sha1).hexdigest()
    if hook_mac == calc_mac:
        if data["status"] == "Credit":
            status = 200
            subject = _("Donation received")
            message = u""
            for (kk, vv) in data.items():
                message += unicode(kk) + u" : " + unicode(vv) + u"\r\n"
            send_mail(
                subject, message,
                settings.DEFAULT_FROM_EMAIL,
                settings.DONATE_EMAIL_RECIPIENTS
            )
    return HttpResponse("", status=status)
