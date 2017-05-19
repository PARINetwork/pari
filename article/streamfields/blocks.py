from wagtail.wagtailadmin import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock


class SingleImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(icon='image')
    caption = blocks.CharBlock()

    class Meta:
        icon = 'image'
        template = 'article/blocks/single_image.html'

