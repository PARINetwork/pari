from django.conf import settings as django_settings
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailcore.models import Site

from .models import HomePage


def settings(request):
    try:
        announcements = HomePage.objects.get().announcements
    except HomePage.DoesNotExist:
        announcements = None
    if not getattr(django_settings, "SOCIAL", None):
        return {}
    try:
        site = Site.objects.get(hostname=request.get_host())
    except Site.DoesNotExist:
        site = None
    return {
        "SOCIAL_FACEBOOK": django_settings.SOCIAL.get("FACEBOOK", ""),
        "SOCIAL_TWITTER": django_settings.SOCIAL.get("TWITTER", ""),
        "SOCIAL_YOUTUBE": django_settings.SOCIAL.get("YOUTUBE", ""),
        "SOCIAL_SOUND_CLOUD": django_settings.SOCIAL.get("SOUND_CLOUD", ""),
        "SOCIAL_GITHUB_REPO": django_settings.SOCIAL.get("GITHUB_REPO", ""),
        "GOOGLE_ANALYTICS_ID": django_settings.SOCIAL.get("GOOGLE_ANALYTICS_ID", ""),
        "SITE_TITLE": django_settings.SITE_TITLE,
        "announcements": announcements,
        "site": site,
    }
