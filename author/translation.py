from modeltranslation.translator import translator, TranslationOptions
from .models import Author


class AuthorOptions(TranslationOptions):
    fields = ('bio', )


translator.register(Author, AuthorOptions)
