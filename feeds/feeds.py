from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed
from django.utils import timezone
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from wagtail.wagtailcore.models import Site

from article.models import Article
from album.models import Album
from face.models import Face
from resources.models import Resource

import itertools
import datetime
import operator
import mimetypes


class BaseFeed(Feed):
    def __init__(self, *args, **kwargs):
        num_days = getattr(settings, "FEED_GENERATION_DAYS", 0)
        self.days_ago = int(num_days)
        super(BaseFeed, self).__init__(*args, **kwargs)

    def __call__(self, request, *args, **kwargs):
        feed_format = request.GET.get("format")
        if feed_format:
            if feed_format == "atom":
                self.feed_type = Atom1Feed
            else:
                self.feed_type = Rss201rev2Feed
        else:
            accept_header = request.META.get("HTTP_ACCEPT", "")
            if accept_header.find("application/atom+xml") >= 0:
                self.feed_type = Atom1Feed
            else:
                self.feed_type = Rss201rev2Feed

        self.language = None
        if request.GET.get("hl"):
            self.language = request.GET["hl"]

        self.request = request
        return super(BaseFeed, self).__call__(request, *args, **kwargs)

    def item_pubdate(self, item):
        return item.first_published_at

    def item_author_name(self, item):
        authors = ""
        if item.__class__.__name__.lower() == "article":
            authors = ",".join(list(item.authors.values_list("name", flat=True)))
        elif item.__class__.__name__.lower() == "album":
            authors = ",".join(set(list(map(lambda slide: ",".join(slide.image.photographers.all().values_list('name', flat=True)),item.slides.all()))))
        return authors

    def item_enclosure_url(self, item):
        if not getattr(item.featured_image, 'file', None):
            url = item.featured_image
        else:
            url = item.featured_image.file.url
            url = "{0}://{1}{2}".format(
                "http" + ("s" if self.request.is_secure() else ""),
                Site.find_for_request(self.request).hostname,
                url
            )
        return url

    def item_enclosure_length(self, item):
        if not getattr(item.featured_image, 'file', None):
            return 0
        try:
            return item.featured_image.file.size
        except IOError:
            return 0

    def item_enclosure_mime_type(self, item):
        url = self.item_enclosure_url(item)
        return mimetypes.guess_type(url)[0] or "application/octet-stream"


class AllFeed(BaseFeed):
    title = _("PARI consolidated feed")
    link = "/feeds/all/"

    def __init__(self, *args, **kwargs):
        super(AllFeed, self).__init__(*args, **kwargs)
        self.description = _("Updates on the PARI site over the "
                             "past {0} days".format(self.days_ago))

    def items(self):
        x_days_ago = timezone.now() - datetime.timedelta(days=self.days_ago)
        x_days_ago = "2016-09-01"
        kwargs = {
            "first_published_at__gte": x_days_ago,
        }
        if self.language:
            kwargs["language"] = self.language
        items_gen = itertools.chain(
            Article.objects.live().filter(**kwargs),
            Album.objects.live().filter(**kwargs),
            Face.objects.live().filter(**kwargs),
            Resource.objects.live().filter(**kwargs),
        )
        return sorted(
            items_gen,
            key=operator.attrgetter('first_published_at'),
            reverse=True)

    def item_description(self, item):
        if item.__class__.__name__.lower() == "article":
            return item.strap
        elif item.__class__.__name__.lower() == "album":
            return item.slides.all()[0].description
        elif item.__class__.__name__.lower() == "resource":
            return item.title
        return item.additional_info or ""



class ArticleFeed(BaseFeed):
    title = _("PARI article feed")
    link = "/feeds/articles/"

    def __init__(self, *args, **kwargs):
        super(ArticleFeed, self).__init__(*args, **kwargs)
        self.description = _("Article updates on the PARI site "
                             "over the past {0} days".format(self.days_ago))

    def items(self):
        x_days_ago = timezone.now() - datetime.timedelta(days=self.days_ago)
        kwargs = {
            "first_published_at__gte": x_days_ago,
        }
        if self.language:
            kwargs["language"] = self.language
        return Article.objects.live().order_by('-first_published_at').filter(**kwargs)

    def item_description(self, item):
        return item.strap


class AlbumFeed(BaseFeed):
    title = _("PARI album feed")
    link = "/feeds/albums/"

    def __init__(self, *args, **kwargs):
        super(AlbumFeed, self).__init__(*args, **kwargs)
        self.description = _("Album updates on the PARI site "
                             "over the past {0} days".format(self.days_ago))

    def items(self):
        x_days_ago = timezone.now() - datetime.timedelta(days=self.days_ago)
        kwargs = {
            "first_published_at__gte": x_days_ago,
        }
        if self.language:
            kwargs["language"] = self.language
        return Album.objects.live().order_by('-first_published_at').filter(**kwargs)

    def item_description(self, item):
        return item.description


class FaceFeed(BaseFeed):
    title = _("PARI face feed")
    link = "/feeds/faces/"

    def __init__(self, *args, **kwargs):
        super(FaceFeed, self).__init__(*args, **kwargs)
        self.description = _("Face updates on the PARI site "
                             "over the past {0} days".format(self.days_ago))

    def items(self):
        x_days_ago = timezone.now() - datetime.timedelta(days=self.days_ago)
        kwargs = {
            "first_published_at__gte": x_days_ago,
        }
        if self.language:
            kwargs["language"] = self.language
        return Face.objects.live().order_by('-first_published_at').filter(**kwargs)

    def item_description(self, item):
        return item.description


class ResourceFeed(BaseFeed):
    title = _("PARI resource feed")
    link = "/feeds/resources/"

    def __init__(self, *args, **kwargs):
        super(ResourceFeed, self).__init__(*args, **kwargs)
        self.description = _("Resource updates on the PARI site over the "
                             "past {0} days".format(self.days_ago))

    def items(self):
        x_days_ago = timezone.now() - datetime.timedelta(days=self.days_ago)
        kwargs = {
            "first_published_at__gte": x_days_ago,
        }
        if self.language:
            kwargs["language"] = self.language
        return Resource.objects.live().order_by('-first_published_at').filter(**kwargs)

    def item_description(self, item):
        return item.title


def feeds_list_page(request):
    return render(request, "feeds/feeds_list.html", {})
