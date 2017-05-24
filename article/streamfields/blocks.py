from wagtail.wagtailadmin import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock()


class FullWidthImageBlock(blocks.StructBlock):
    image = ImageBlock()

    class Meta:
        icon = 'image'
        template = 'article/blocks/full_width_image.html'


class TwoColumnImageBlock(blocks.StructBlock):
    image_left = ImageBlock()
    image_right = ImageBlock()

    class Meta:
        icon = 'image'
        template = 'article/blocks/two_column_image.html'


class RichTextBlock(blocks.StructBlock):
    content = blocks.RichTextBlock()

    class Meta:
        icon='doc-full'
        template = 'article/blocks/rich_text.html'
