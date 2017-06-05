import json
import os
import sys

from bs4 import BeautifulSoup
import django

if '__file__' in locals():
    sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

django.setup()

from article.models import Article


class ArticleMigrator(object):
    def __init__(self, article):
        self.article = article
        self.unhandled_elements = []
        self.modular_content = []
        self.content = BeautifulSoup(self.article.content).find('body').extract().contents

    def formulate_modular_content(self):
        paragraph_collector = []

        for element in self.content:
            if element.name in (None, 'br'):
                continue

            if element.name != 'p':
                self.unhandled_elements.append(element.name)
                continue

            # paragraph_images = element.find_all('img')
            paragraph_embeded_images = element.find_all('embed', attrs={'embedtype': 'image'})

            if not paragraph_embeded_images:
                paragraph_collector += str(element)
            elif len(paragraph_embeded_images) == 1:
                if paragraph_collector:
                    self.modular_content.append(Module.paragraph("".join(paragraph_collector)))
                    paragraph_collector = []

                img = element.find('embed')
                image_id = img.attrs.get('id')
                if image_id:
                    caption = img.attrs['alt'] or 'Caption place holder'
                    alignment = img.attrs.get('format')
                    img.decompose()
                    self.modular_content.append(Module.paragraph_with_image(str(element), image_id, caption, alignment))
            else:
                self.unhandled_elements.append('More than one images in  a pargraph')
                continue

        if paragraph_collector:
            self.modular_content.append(Module.paragraph("".join(paragraph_collector)))

        return self

    def save_revision(self):
        self.article.modular_content = json.dumps(self.modular_content)
        self.article.save_revision()


class Module(object):
    @staticmethod
    def full_width_image(image_id, caption):
        return {"type": "full_width_image",
                "value": {
                    "image": Module.image(image_id, caption)
                }}

    @staticmethod
    def paragraph(content):
        return {"type": "paragraph",
                "value": Module.rich_text(content)
                }

    @staticmethod
    def paragraph_with_image(content, image_id, caption, align_image):
        return {"type": "paragraph_with_image",
                "value": {
                    "content": Module.rich_text(content),
                    "align_image": align_image,
                    "image": Module.image(image_id, caption),
                }}

    @staticmethod
    def image(image_id, caption):
        return {
            "caption": caption,
            "image": image_id
        }

    @staticmethod
    def rich_text(content):
        return {"content": content}


if __name__ == '__main__':
    article = Article.objects.live().get(page_ptr_id=2689)
    print article, article.page_ptr_id
    ArticleMigrator(article).formulate_modular_content().save_revision()
