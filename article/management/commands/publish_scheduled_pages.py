from __future__ import absolute_import, print_function, unicode_literals

from django.core.management.base import BaseCommand
from django.utils import timezone

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.management.commands.publish_scheduled_pages import Command as BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)
        for page in Page.objects.filter(go_live_at__lte=timezone.now()):
            if not page.live:
                page.publish()
