from wagtailtinymce.rich_text import TinyMCERichTextArea


class TinyMCECustomTextArea(TinyMCERichTextArea):

    def __init__(self,**kwargs):
        self.buttons = ['bold', 'italic']
        super(TinyMCECustomTextArea, self).__init__(buttons=[[['bold', 'italic']]])