from enum import Enum


class TinyMCEFormatingButtons(Enum):

    CHARACTER_STYLING = ['bold', 'italic']
    UNDO_REDO= ['undo', 'redo']
    STYLESELECT=[ 'styleselect' ]
    LISTING=[ 'bullist', 'numlist', 'outdent', 'indent' ]
    TABLE=[ 'table' ]
    LINK=['link', 'unlink']
    WAGTAIL_FEATURES=['wagtaildoclink', 'wagtailimage', 'wagtailembed']
    MISCELLANEOUS=['pastetext', 'fullscreen']
    HORIZONTAL_RULE = ['hr']

    def __str__(self):
        return str(self.value)