import json
import os
import sys

import django

from bs4 import BeautifulSoup
from django.db.models import Q

if '__file__' in locals():
    sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

django.setup()

from article.models import Article
from core.models import AffixImage
from django.conf import settings


class ArticleMigrator(object):
    def __init__(self, article):
        self.article = article
        self.unhandled_elements = []
        self.modular_content = []
        self.paragraph_collector = []
        self.content = BeautifulSoup(self.article.content).find('body').extract().contents

    def formulate_modular_content(self):
        for element in self.content:
            if element.name in (None, 'br'):
                continue

            if element.name == 'img':
                self._flush_collected_paragraphs_to_module()
                self._add_full_width_image_module(element)
            elif element.name == 'p':
                embedded_images = element.find_all('embed', attrs={'embedtype': 'image'})
                other_images = element.find_all(lambda tag: tag.name == 'img' and not tag.has_attr('embedtype'))

                if other_images and embedded_images:
                    self.unhandled_elements.append("Paragraph has both embedded and full-width images")
                elif not embedded_images and not other_images:
                    self.paragraph_collector += str(element)
                elif len(embedded_images) == 1:
                    self._flush_collected_paragraphs_to_module()
                    self._add_image_with_paragraph_module(element)
                elif len(other_images) == 1:
                    self._flush_collected_paragraphs_to_module()
                    img = element.find('img')
                    self._add_full_width_image_module(img)
                    img.decompose()
                    text = element.getText().strip()
                    if text:
                        self.modular_content.append(Module.paragraph(str(element)))
                else:
                    self.unhandled_elements.append('Paragraph has more than one images/embedded-images')
            else:
                self.unhandled_elements.append(element.name)

        self._flush_collected_paragraphs_to_module()
        return self

    def save_revision(self):
        self.article.modular_content = json.dumps(self.modular_content)
        self.article.save_revision()
        return self

    def _add_full_width_image_module(self, img):
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
        if image:
            self.modular_content.append(Module.full_width_image(image.id, caption))
        else:
            self.unhandled_elements.append("Unable to find image with src: %s" % image_file)

    def _add_image_with_paragraph_module(self, element):
        img = element.find('embed')
        image_id = img.attrs.get('id')
        if image_id:
            caption = img.attrs['alt'] or ''
            alignment = img.attrs.get('format')
            img.decompose()
            self.modular_content.append(Module.paragraph_with_image(str(element), image_id, caption, alignment))
        else:
            self.unhandled_elements.append("Embeded image has no ID")

    def _flush_collected_paragraphs_to_module(self):
        if self.paragraph_collector:
            paragraphs = "".join(self.paragraph_collector)
            self.modular_content.append(Module.paragraph(paragraphs))
            self.paragraph_collector = []


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
        print article.page_ptr_id, article,
        article_ = ArticleMigrator(article).formulate_modular_content().save_revision()
        print  article_.unhandled_elements
