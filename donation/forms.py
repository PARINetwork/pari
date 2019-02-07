from django import forms
from django.utils.translation import ugettext_lazy as _

from .fields import AmountField
from .helpers import DonationOptions


class DonateForm(forms.Form):
    amount = AmountField(
        choices=DonationOptions.Amount.CHOICES,
        label=_('Amount')
    )
    frequency = forms.ChoiceField(
        choices=DonationOptions.Frequency.FORM_CHOICES,
        widget=forms.RadioSelect
    )
    name = forms.CharField(
        label=_("NAME"),
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        label=_("EMAIL"),
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    phone = forms.CharField(
        label=_("PHONE NUMBER"),
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    address = forms.CharField(
        label=_("ADDRESS"),
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        required=False
    )
    pan = forms.CharField(
        label=_("PAN NUMBER"),
        max_length=10,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        help_text=_("PAN is required as per government regulations.")
    )
    is_indian = forms.BooleanField(
        initial=False,
        label=_("I declare that I am an Indian citizen"),
        widget=forms.CheckboxInput(),
        help_text=_("At this moment, we can accept donations from Indians only")
    )

    def clean_is_indian(self):
        data = self.cleaned_data["is_indian"]
        if data != True:
            raise forms.ValidationError(_("Sorry, we can accept donations "
                                          "from Indians only."))
        return data
