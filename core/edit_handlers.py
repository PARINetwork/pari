from wagtail.wagtailadmin.edit_handlers import BaseFieldPanel, FieldPanel


class BaseM2MFieldPanel(BaseFieldPanel):
    object_template = "core/edit_handlers/single_field_panel.html"
    
class M2MFieldPanel(FieldPanel):
    def bind_to_model(self, model):
        base = {
            'model': model,
            'field_name': self.field_name,
            'classname': self.classname,
        }

        if self.widget:
            base['widget'] = self.widget

        return type(str('_M2MFieldPanel'), (BaseM2MFieldPanel,), base)


class BaseAudioFieldPanel(BaseFieldPanel):
    field_template = "core/edit_handlers/audio_panel.html"
    
class AudioPanel(FieldPanel):
    def bind_to_model(self, model):
        base = {
            'model': model,
            'field_name': self.field_name,
            'classname': self.classname,
        }

        if self.widget:
            base['widget'] = self.widget

        return type(str('_AudioPanel'), (BaseAudioFieldPanel,), base)
