from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        exclude = ("created_on",)
        model = Contact


class DonateForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
    pan = forms.CharField(
        label=_("PAN"),
        max_length=10,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        help_text=_("PAN is required as per government regulations.")
    )
    is_indian = forms.BooleanField(
        initial = False,
        label=_("I hereby declare that I am an Indian"),
        widget=forms.CheckboxInput(),
        help_text=_("At this moment, we can accept donations from Indians only")
    )

    def clean_is_indian(self):
        data = self.cleaned_data["is_indian"]
        if data != True:
            raise forms.ValidationError(_("Sorry, we can accept donations "
                                          "from Indians only."))
        return data
