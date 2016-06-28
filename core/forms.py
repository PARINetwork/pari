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
    pan_number = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        help_text=_("Required as per government regulations.")
    )
    amount = forms.IntegerField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
