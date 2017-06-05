import json
import os
import sys

from bs4 import BeautifulSoup
import django
from django.db.models import Q

if '__file__' in locals():
    sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

django.setup()

from django.conf import settings
from article.models import Article

from core.models import AffixImage


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

            embedded_images = element.find_all('embed', attrs={'embedtype': 'image'})
            images = element.find_all(lambda tag: tag.name == 'img' and not tag.has_attr('embedtype'))

            if images and embedded_images:
                self.unhandled_elements.append("Has both embedded and full-width images")
                continue

            if not embedded_images and not images:
                paragraph_collector += str(element)
            elif len(embedded_images) == 1:
                if paragraph_collector:
                    self.modular_content.append(Module.paragraph("".join(paragraph_collector)))
                    paragraph_collector = []

                img = element.find('embed')
                image_id = img.attrs.get('id')
                if image_id:
                    caption = img.attrs['alt'] or ''
                    alignment = img.attrs.get('format')
                    img.decompose()
                    self.modular_content.append(Module.paragraph_with_image(str(element), image_id, caption, alignment))
                else:
                    self.unhandled_elements.append("Embeded image has no ID")
            elif len(images) == 1:
                if paragraph_collector:
                    self.modular_content.append(Module.paragraph("".join(paragraph_collector)))
                    paragraph_collector = []

                img = element.find('img')

                image_src = img.attrs.get('src')
                image_srcset = img.attrs.get('srcset')

                if image_src:
                    image_file = image_src[len(settings.MEDIA_URL):]
                elif image_srcset:
                    image_file = image_srcset.split()[0][len(settings.MEDIA_URL):]
                else:
                    raise NotImplementedError

                image = AffixImage.objects.filter(Q(file=image_file) | Q(renditions__file=image_file)).first()
                caption = img.attrs.get('alt') or ''
                img.decompose()

                if image:
                    self.modular_content.append(Module.full_width_image(image.id, caption))
                else:
                    self.unhandled_elements.append("Unable to find image with src: %s" % image_file)

                text = element.getText().strip()
                if text:
                    self.modular_content.append(Module.paragraph(str(element)))
            else:
                self.unhandled_elements.append('More than one images/embedded-images in a pargraph')
                continue

        if paragraph_collector:
            self.modular_content.append(Module.paragraph("".join(paragraph_collector)))

        return self

    def save_revision(self):
        self.article.modular_content = json.dumps(self.modular_content)
        self.article.save_revision()
        return self


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
    for article in Article.objects.live().all():
        print article.page_ptr_id, article
        article_ = ArticleMigrator(article).formulate_modular_content().save_revision()
        if article_.unhandled_elements:
            print  article_.unhandled_elements
