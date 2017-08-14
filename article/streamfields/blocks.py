from django import forms
from django.utils.functional import cached_property
from wagtail.wagtailadmin import blocks
from wagtail.wagtailcore.blocks import PageChooserBlock, RichTextBlock, FieldBlock, URLBlock, RawHTMLBlock
from wagtail.wagtailcore.models import Page
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from article.rich_text import get_rich_text_editor_widget
from face.models import Face
from location.models import Location


class CustomRichTextBlock(RichTextBlock):
    @cached_property
    def field(self):
        return forms.CharField(widget=get_rich_text_editor_widget(self.editor), **self.field_options)


# TODO: This is implemented in the latest wagtail. Remove it after upgrading.
class IntegerBlock(FieldBlock):
    def __init__(self, required=True, help_text=None, min_value=None,
                 max_value=None, **kwargs):
        self.field = forms.IntegerField(
            required=required,
            help_text=help_text,
            min_value=min_value,
            max_value=max_value
        )
        super(IntegerBlock, self).__init__(**kwargs)

    class Meta:
        icon = "plus-inverse"


class ModelMultipleChoiceBlock(FieldBlock):
    def __init__(self, target_model, required=True, help_text=None, **kwargs):
        self.target_model = target_model
        self.field = forms.ModelMultipleChoiceField(
            queryset=self.target_model.objects.all(),
            required=required,
            help_text=help_text,
        )
        super(ModelMultipleChoiceBlock, self).__init__(**kwargs)

    def to_python(self, value):
        if not value:
            return value
        else:
            return self.target_model.objects.filter(pk__in=value)

    def get_prep_value(self, value):
        if not value:
            return value
        else:
            return [each.pk for each in value]

    def value_from_form(self, value):
        if not value or all(isinstance(each, self.target_model) for each in value):
            return value
        else:
            return self.target_model.objects.filter(pk__in=value)

    def value_for_form(self, value):
        if not value:
            return value
        elif all(isinstance(each, self.target_model) for each in value):
            return [each.pk for each in value]
        else:
            return []


# TODO implement caption in the block it is implemented in.
class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()

    class Meta:
        icon = 'image'
        template = 'article/blocks/image.html'


class PageTypeChooserBlock(PageChooserBlock):
    """Custom implementation of PageChooserBlock to limit page selection to specific page types.
    Note: This has been addressed in the latest wagtail version.
    """

    def __init__(self, for_models=[Page], **kwargs):
        if any(not issubclass(each, Page) for each in for_models):
            raise TypeError("All models passed should be a sub-class of wagtail.wagtailcore.models.Page")
        self.for_models = for_models
        super(PageTypeChooserBlock, self).__init__(**kwargs)

    @cached_property
    def target_model(self):
        if len(self.for_models) == 1:
            return self.for_models[0]
        else:
            from wagtail.wagtailcore.models import Page
            return Page

    @cached_property
    def widget(self):
        from django.utils.translation import ugettext_lazy as _
        from wagtail.wagtailadmin.widgets import AdminPageChooser

        model_names = ' / '.join(each.__name__.lower() for each in self.for_models)
        admin_page_chooser = AdminPageChooser(target_models=self.for_models)
        admin_page_chooser.choose_one_text = _('Choose a %s' % model_names)
        admin_page_chooser.choose_another_text = _('Choose another %s' % model_names)
        admin_page_chooser.link_to_chosen_text = _('Edit this %s' % model_names)
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
    ALIGN_CONTENT_CHOICES = [('default', 'Default'), ('center', 'Center')]

    content = CustomRichTextBlock(editor='hallo_for_paragraph')
    align_content = blocks.ChoiceBlock(choices=ALIGN_CONTENT_CHOICES, default=ALIGN_CONTENT_CHOICES[0][0])

    class Meta:
        icon = 'doc-full'
        label = 'Paragraph Module'
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
    face = PageTypeChooserBlock(for_models=[Face])

    class Meta:
        icon = 'image'
        template = 'article/blocks/face.html'


class ParagraphWithBlockQuoteBlock(blocks.StructBlock):
    ALIGN_QUOTE_CHOICES = [('left', 'Left Column'), ('right', 'Right Column')]

    quote = CustomRichTextBlock(editor='hallo_for_quote')
    align_quote = blocks.ChoiceBlock(choices=ALIGN_QUOTE_CHOICES, default=ALIGN_QUOTE_CHOICES[1][0])
    content = ParagraphBlock()

    class Meta:
        icon = 'doc-full'
        label = 'Paragraphs with Block Quote'
        template = 'article/blocks/paragraph_with_block_quote.html'


class FullWidthBlockQuote(blocks.StructBlock):
    quote = CustomRichTextBlock(editor='hallo_for_quote')

    class Meta:
        icon = 'doc-full'
        label = 'Full width Block Quote'
        template = 'article/blocks/full_width_block_quote.html'


class NColumnParagraphBlock(blocks.StructBlock):
    paragraph = blocks.ListBlock(ParagraphBlock())

    class Meta:
        template = 'article/blocks/columnar_paragraph.html'
        label = 'Columnar Paragraphs'


class ParagraphWithEmbedBlock(blocks.StructBlock):
    ALIGN_EMBED_CHOICES = [('left', 'Left'), ('right', 'Right')]

    embed = URLBlock()
    embed_max_width = IntegerBlock(required=False, help_text="Optional field. Maximum width of the content in pixels to"
                                                             " be requested from the content provider(e.g YouTube). "
                                                             "If the requested width is not supported, provider will be"
                                                             " supplying the content with nearest available width.")
    embed_align = blocks.ChoiceBlock(choices=ALIGN_EMBED_CHOICES, default=ALIGN_EMBED_CHOICES[0][0])
    content = ParagraphBlock()

    class Meta:
        icon = 'media'
        label = 'Paragraphs with embed'
        template = 'article/blocks/paragraph_with_embed.html'


class NColumnImageBlock(blocks.StructBlock):
    images = blocks.ListBlock(ImageBlock())
    height = IntegerBlock(min_value=0, required=True, default=380)
    caption = blocks.CharBlock(required=False)

    def get_context(self, value):
        context = super(NColumnImageBlock, self).get_context(value)
        context['height'] = value['height']
        return context

    class Meta:
        template = 'article/blocks/columnar_image.html'
        label = 'Columnar Images'


class ParagraphWithRawEmbedBlock(blocks.StructBlock):
    ALIGN_EMBED_CHOICES = [('left', 'Left'), ('right', 'Right')]

    embed = RawHTMLBlock(help_text="Embed HTML code(an iframe)")
    embed_align = blocks.ChoiceBlock(choices=ALIGN_EMBED_CHOICES, default=ALIGN_EMBED_CHOICES[0][0])
    content = ParagraphBlock()

    class Meta:
        icon = 'media'
        label = 'Paragraphs with raw embed'
        template = 'article/blocks/paragraph_with_raw_embed.html'


class FullWidthEmbedBlock(blocks.StructBlock):
    embed = EmbedBlock(required=True, help_text="Enter URL for the embed block")

    class Meta:
        icon = 'media'
        label = 'Full width embed'
        template = 'article/blocks/full_width_embed.html'


class VideoWithQuoteBlock(blocks.StructBlock):
    ALIGN_QUOTE_CHOICES = [('left', 'Left Column'), ('right', 'Right Column')]

    video = EmbedBlock(help_text="YouTube video URL")
    quote = CustomRichTextBlock(editor='hallo_for_quote')
    align_quote = blocks.ChoiceBlock(choices=ALIGN_QUOTE_CHOICES, default=ALIGN_QUOTE_CHOICES[0][1])

    class Meta:
        icon = 'doc-full'
        label = 'Video with Block Quote'
        template = 'article/blocks/video_with_block_quote.html'


class ParagraphWithMapBlock(blocks.StructBlock):
    content = ParagraphBlock()
    locations = ModelMultipleChoiceBlock(target_model=Location)

    class Meta:
        label = 'Paragraphs with map'
