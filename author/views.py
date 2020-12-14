from django.shortcuts import render
from django.utils.text import slugify
from django.urls import reverse
from django.http import HttpResponseRedirect

from wagtail.admin.modal_workflow import render_modal_workflow

from .forms import AuthorAdminForm


def get_result(instance):
    if instance:
        return {
            'id': instance.id,
            'name': instance.name
        }
    else:
        return None


def add_author(request):
    instance = None
    if request.method == "POST":
        form = AuthorAdminForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.slug = slugify(instance.name)
            instance.save()
    else:
        form = AuthorAdminForm()
    return render_modal_workflow(
        request,
        "core/add_object.html",
        None,
        {
            "add_object_url": reverse("author_add"),
            "name": "Author",
            "form": form,
            "instance": instance
        },
        json_data={
            "step": "chooser",
            "result": get_result(instance)
        }
    )


def add_translator(request):
    return HttpResponseRedirect(reverse("author_add"))

def add_photographer(request):
    return HttpResponseRedirect(reverse("author_add"))
