from django.utils.html import escape

from wagtail.wagtailimages.formats import register_image_format, \
    unregister_image_format, Format
from wagtail.wagtailimages.models import SourceImageIOError


class LazyImgFormat(Format):
    def image_to_editor_html(self, image, alt_text, extra_attributes=''):
        return self.image_to_html(image, alt_text, extra_attributes)

    def image_to_html(self, image, alt_text, extra_attributes=''):
        try:
            rendition = image.get_rendition(self.filter_spec)
        except SourceImageIOError:
            # Image file is (probably) missing from /media/original_images - generate a dummy
            # rendition so that we just output a broken image, rather than crashing out completely
            # during rendering
            Rendition = image.renditions.model  # pick up any custom Image / Rendition classes that may be in use
            rendition = Rendition(image=image, width=0, height=0)
            rendition.file.name = 'not-found'

        try:
            half_rendition = image.get_rendition('max-512x410')
        except SourceImageIOError:
            # Image file is (probably) missing from /media/original_images - generate a dummy
            # rendition so that we just output a broken image, rather than crashing out completely
            # during rendering
            Rendition = image.renditions.model  # pick up any custom Image / Rendition classes that may be in use
            half_rendition = Rendition(image=image, width=0, height=0)
            half_rendition.file.name = 'not-found'

        if self.classnames:
            class_attr = 'class="%s" ' % escape(self.classnames)
        else:
            class_attr = ''

        sizes = "(max-width: 480px) 512w, 100vw"
        srcset = "%s 512w, %s" % (escape(half_rendition.url),
                                  escape(rendition.url))
        return ('<img %s%s '
                'width="%d" height="%d" '
                'alt="%s" srcset="%s" sizes="%s">') % (
                    extra_attributes, class_attr,
                    rendition.width, rendition.height, alt_text,
                    srcset, sizes
                )


register_image_format(Format('halfwidth', 'Half Width (512px)', 'richtext-image half-width', 'max-512x410'))
unregister_image_format("fullwidth")
register_image_format(LazyImgFormat('fullwidth', 'Full width', 'richtext-image full-width', 'max-1400x1120'))
