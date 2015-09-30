from django.shortcuts import render
from django.http import Http404
from django.contrib.messages import success
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.models import Page

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
