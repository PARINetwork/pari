import re

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django import forms
from django.db import models


class CoreAppConfig(AppConfig):
    name = "core"

    def ready(self):
        from . import signal_handlers
        super(CoreAppConfig, self).ready()

# Code below is monkey-patching django to support unicode slugs
# Will have to remove when django supports unicode slugs by default
slug_re = re.compile(ur'^[-_\w]+', re.U)
validate_slug = validators.RegexValidator(
    slug_re,
    _("Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens."),
    'invalid'
)
validators.slug_re = slug_re
validators.validate_slug = validate_slug


class FormSlugField(forms.SlugField):
    default_validators = [validate_slug]
forms.SlugField = FormSlugField

class ModelSlugField(models.SlugField):
    default_validators = [validate_slug]
models.SlugField = ModelSlugField
