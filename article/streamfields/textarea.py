from wagtailtinymce.rich_text import TinyMCERichTextArea


class TinyMCECustomTextArea(TinyMCERichTextArea):

    def __init__(self,**kwargs):
        super(TinyMCECustomTextArea, self).__init__(**kwargs)