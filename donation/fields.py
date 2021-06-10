
# Credit https://djangosnippets.org/snippets/863/

from django import forms
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

VALUE_ERROR_MSG = "expecting item[0] of last choice to be 'Other'"


class AmountWidget(forms.MultiWidget):
    class Media:
        js = ('donation/js/amount_widget.js',)

    def __init__(self, choices):
        if choices[-1][0].lower() != 'other':
            raise ValueError(VALUE_ERROR_MSG)
        widgets = [
            forms.RadioSelect(choices=choices),
            forms.TextInput(attrs={
                'placeholder': 'Other Amount',
                'class': 'other-amount',
                'onfocus': "this.placeholder=''",
                'onblur': "this.placeholder='Other Amount'"
            })
        ]
        super(AmountWidget, self).__init__(widgets)

    def decompress(self, value):
        if not value:
            return [None, None]
        return value

    def render(self, name, value, attrs=None, renderer=None):
        if self.is_localized:
            for widget in self.widgets:
                widget.is_localized = self.is_localized
        if not isinstance(value, list):
            value = self.decompress(value)
        output = []
        final_attrs = self.build_attrs(attrs)
        id_ = final_attrs.get('id')
        for i, widget in enumerate(self.widgets):
            try:
                widget_value = value[i]
            except IndexError:
                widget_value = None
            if id_:
                final_attrs = dict(final_attrs, id='%s_%s' % (id_, i))
            output.append(widget.render(name + '_%s' % i, widget_value, final_attrs))
        insert_idx = output[0].rindex('</label>\n\n</li>\n</ul>')
        return mark_safe(output[0][:insert_idx] + output[1] + output[0][insert_idx:])

class AmountField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        fields = [
            forms.ChoiceField(*args, **kwargs),
            forms.IntegerField(required=False, min_value=1)
        ]
        widget = AmountWidget(choices=kwargs['choices'])
        kwargs.pop('choices')
        self._was_required = kwargs.pop('required', True)
        kwargs['required'] = False
        super(AmountField, self).__init__(widget=widget, fields=fields, *args, **kwargs)

    def compress(self, value):
        if not value:
            return None

        return value[1] \
            if force_text(value[0]) == force_text(self.fields[0].choices[-1][0]) \
            else int(value[0])
