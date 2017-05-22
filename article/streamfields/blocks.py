from wagtail.wagtailadmin import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock


class FullWidthImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(icon='image')
    caption = blocks.CharBlock()

    class Meta:
        icon = 'image'
        template = 'article/blocks/full_width_image.html'


class TwoColumnImageBlock(blocks.StructBlock):
    image_left = ImageChooserBlock()
    caption_left = blocks.CharBlock()
    image_right = ImageChooserBlock()
    caption_right = blocks.CharBlock()

    class Meta:
        icon = 'image'
        template = 'article/blocks/two_column_image.html'


class RichTextBlock(blocks.StructBlock):
    content = blocks.RichTextBlock()

    class Meta:
        template = 'article/blocks/rich_text.html'
