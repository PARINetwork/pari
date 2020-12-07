from wagtail.admin.edit_handlers import FieldPanel

#
# class BaseM2MFieldPanel(FieldPanel):
#     object_template = "core/edit_handlers/single_field_panel.html"


class M2MFieldPanel(FieldPanel):
    def __init__(self, *args, **kwargs):
        self.field_template = "core/edit_handlers/single_field_panel.html"
        super().__init__(*args, **kwargs)

    def clone(self):
        return self.__class__(
            heading=self.heading,
            classname=self.classname,
            help_text=self.help_text,
            field_name=self.field_name
        )


# class BaseAudioFieldPanel(FieldPanel):
#     field_template = "core/edit_handlers/audio_panel.html"


class AudioPanel(FieldPanel):
    def __init__(self, *args, **kwargs):
        self.field_template = "core/edit_handlers/audio_panel.html"
        super().__init__(*args, **kwargs)

    def clone(self):
        return self.__class__(
            heading=self.heading,
            classname=self.classname,
            help_text=self.help_text,
            field_name=self.field_name
        )
