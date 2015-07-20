from django import forms

from wagtail.wagtailimages.widgets import AdminImageChooser

from .models import Author


class AuthorAdminForm(forms.ModelForm):
    class Meta:
        model = Author
        # TODO: Ability to add author image
        exclude = ['image', 'slug']
