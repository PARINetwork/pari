from django.conf import settings as django_settings

def settings(request):
    if not getattr(django_settings, "SOCIAL", None):
        return {}
    return {
        "SOCIAL_FACEBOOK": django_settings.SOCIAL.get("FACEBOOK", ""),
        "SOCIAL_TWITTER": django_settings.SOCIAL.get("TWITTER", ""),
        "SOCIAL_GITHUB_REPO": django_settings.SOCIAL.get("GITHUB_REPO", ""),
        "GOOGLE_ANALYTICS_ID": django_settings.SOCIAL.get("GOOGLE_ANALYTICS_ID", ""),
    }
