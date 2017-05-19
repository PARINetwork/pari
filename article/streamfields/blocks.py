from wagtail.wagtailadmin import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock


class FullWidthImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(icon='image')
    caption = blocks.CharBlock()

    class Meta:
        icon = 'image'
        template = 'article/blocks/full_width_image.html'

