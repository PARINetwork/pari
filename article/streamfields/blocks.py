from django.utils.functional import cached_property

from wagtail.wagtailadmin import blocks
from wagtail.wagtailcore.blocks import PageChooserBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock()

    class Meta:
        icon = 'image'
        template = 'article/blocks/image.html'


class FaceChooserBlock(PageChooserBlock):
    def __init__(self, can_choose_root=False, **kwargs):
        super(FaceChooserBlock, self).__init__(can_choose_root=can_choose_root, **kwargs)

    @cached_property
    def target_model(self):
        from face.models import Face
        return Face

    @cached_property
    def widget(self):
        from django.utils.translation import ugettext_lazy as _
        from wagtail.wagtailadmin.widgets import AdminPageChooser
        from face.models import Face

        admin_face_chooser = AdminPageChooser(target_models=[Face], can_choose_root=self.can_choose_root)
        admin_face_chooser.choose_one_text = _('Choose a face')
        admin_face_chooser.choose_another_text = _('Choose another face')
        admin_face_chooser.link_to_chosen_text = _('Edit this face')
        return admin_face_chooser


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
