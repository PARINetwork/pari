from django.utils.functional import cached_property

from wagtail.wagtailadmin import blocks
from wagtail.wagtailcore.blocks import PageChooserBlock
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.blocks import ImageChooserBlock

from face.models import Face


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock()

    class Meta:
        icon = 'image'
        template = 'article/blocks/image.html'


class PageTypeChooserBlock(PageChooserBlock):
    """Custom implementation of PageChooserBlock to limit page selection to specific page types.
    Note: This has been addressed in the latest wagtail version.
    """

    def __init__(self, for_model, **kwargs):
        if not issubclass(for_model, Page):
            raise TypeError("for_model should be a sub-class of wagtail.wagtailcore.models.Page")
        self.for_model = for_model
        super(PageTypeChooserBlock, self).__init__(**kwargs)

    @cached_property
    def target_model(self):
        return self.for_model

    @cached_property
    def widget(self):
        from django.utils.translation import ugettext_lazy as _
        from wagtail.wagtailadmin.widgets import AdminPageChooser

        model_name = self.for_model.__name__.lower()
        admin_page_chooser = AdminPageChooser(target_models=[self.for_model])
        admin_page_chooser.choose_one_text = _('Choose a %s' % model_name)
        admin_page_chooser.choose_another_text = _('Choose another %s' % model_name)
        admin_page_chooser.link_to_chosen_text = _('Edit this %s' % model_name)
        return admin_page_chooser


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


class ParagraphBlock(blocks.StructBlock):
    content = blocks.RichTextBlock()

    class Meta:
        icon = 'doc-full'
        label = 'Paragraphs'
        template = 'article/blocks/paragraph.html'


class ParagraphWithImageBlock(blocks.StructBlock):
    ALIGN_IMAGE_CHOICES = [('left', 'Left'), ('right', 'Right')]

    image = ImageBlock()
    align_image = blocks.ChoiceBlock(choices=ALIGN_IMAGE_CHOICES, default=ALIGN_IMAGE_CHOICES[0][0])
    content = ParagraphBlock()

    class Meta:
        icon = 'doc-full'
        label = 'Paragraphs with an image'
        template = 'article/blocks/paragraph_with_image.html'


class FaceBlock(blocks.StructBlock):
    face = PageTypeChooserBlock(for_model=Face)

    class Meta:
        icon = 'image'
        template = 'article/blocks/face.html'
