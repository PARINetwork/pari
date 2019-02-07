
# Credit https://djangosnippets.org/snippets/863/

from django import forms
from django.utils.encoding import force_unicode


class AmountWidget(forms.MultiWidget):
    def __init__(self, choices):
        widgets = [
            forms.RadioSelect(choices=choices),
            forms.TextInput
        ]
        super(AmountWidget, self).__init__(widgets)

    def decompress(self, value):
        if not value:
            return [None, None]
        return value

    def format_output(self, rendered_widgets):
        insert_idx = rendered_widgets[0].rindex('</label></li></ul>')
        return rendered_widgets[0][:insert_idx] + rendered_widgets[1] + rendered_widgets[0][insert_idx:]


class AmountField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        fields = [
            forms.ChoiceField(widget=forms.RadioSelect, *args, **kwargs),
            forms.IntegerField(required=False, min_value=1)
        ]
        widget = AmountWidget(choices=kwargs['choices'])
        kwargs.pop('choices')
        self._was_required = kwargs.pop('required', True)
        kwargs['required'] = False
        super(AmountField, self).__init__(widget=widget, fields=fields, *args, **kwargs)

    def compress(self, value):
        if self._was_required and not value or value[0] in (None, ''):
            raise forms.ValidationError(self.error_messages['required'])
        if not value:
            return [None, None]

        return value[0], \
               value[1] if force_unicode(value[0]) == force_unicode(self.fields[0].choices[-1][0]) else u''
