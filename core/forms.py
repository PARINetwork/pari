from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        exclude = ("created_on",)
        model = Contact
