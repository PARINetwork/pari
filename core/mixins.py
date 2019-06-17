from django.core.paginator import InvalidPage
from django.db import models
from django.http import Http404
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView


class TimestampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Page1Redirector(object):
    def get(self, request, *args, **kwargs):
        page = int(request.GET.get('page', 0))
        if page == 1:  # https://github.com/PARINetwork/pari/issues/391#issuecomment-501206067
            return redirect(request.path)
        return super(Page1Redirector, self).get(request, *args, **kwargs)
