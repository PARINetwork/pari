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

DEFAULT_ALIGNMENT = 'left'
EMPTY_CONTENT = ''
DEFAULT_HEIGHT = 380


class ArticleMigrator(object):
    def __init__(self, article):
        self.article = article
        self.unhandled_elements = []
        self.modular_content = []
        self.paragraph_collector = []
        self.structured_content = BeautifulSoup(self.article.content).prettify()
        self.content = BeautifulSoup(self.structured_content).find('body').extract().contents

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
                elif len(other_images) > 1:
                    self._flush_collected_paragraphs_to_module()
                    columnar_image_ids = []
                    for img in other_images:
                        image, image_file = self._get_image_from_img_element(img)
                        if image:
                            columnar_image_ids.append(image.id)
                        else:
                            self.unhandled_elements.append("Unable to find image with src: %s" % image_file)
                    caption = other_images[0].attrs['alt'] or ''
                    height = other_images[0].attrs['height'] or DEFAULT_HEIGHT
                    self.modular_content.append(
                        Module.columnar_image_with_text(EMPTY_CONTENT, columnar_image_ids, caption, DEFAULT_ALIGNMENT,
                                                        height))
                else:
                    self.unhandled_elements.append('Paragraph has more than one images/embedded-images')
            elif element.name == 'embed':
                attr_name = element.attrs.get('embedtype')
                if attr_name == 'image':
                    self._flush_collected_paragraphs_to_module()
                    self._add_image_with_paragraph_module(element, embed=True)
                elif attr_name == 'media':
                    self._flush_collected_paragraphs_to_module()
                    self._add_embed_module(element)
                else:
                    self.unhandled_elements.append("Embed element couldn't be recognised.")
            else:
                self.unhandled_elements.append(element.name)

        self._flush_collected_paragraphs_to_module()
        return self

    def save_revision(self):
        self.article.modular_content = json.dumps(self.modular_content)
        self.article.save_revision()
        return self

    def _add_full_width_image_module(self, img):
        image, image_file = self._get_image_from_img_element(img)
        caption = img.attrs.get('alt') or ''
        if image:
            self.modular_content.append(Module.full_width_image(image.id, caption))
        else:
            self.unhandled_elements.append("Unable to find image with src: %s" % image_file)

    def _get_image_from_img_element(self, img):
        image_src = img.attrs.get('src')
        image_srcset = img.attrs.get('srcset')
        if image_src:
            image_file = image_src[len(settings.MEDIA_URL):]
        elif image_srcset:
            image_file = image_srcset.split()[0][len(settings.MEDIA_URL):]
        else:
            raise NotImplementedError
        if str(image_file).startswith('/ruralindiaonline.org/'):
            image_file = image_file[28:].replace('%20', " ")
        image = AffixImage.objects.filter(Q(file=image_file) | Q(renditions__file=image_file)).first()
        return image, image_file

    def _add_image_with_paragraph_module(self, element, embed=False):
        if not embed:
            img = element.find('embed')
        else:
            img = element
        image_id = img.attrs.get('id')
        if image_id:
            caption = img.attrs['alt'] or ''
            alignment = img.attrs.get('format')
            img.decompose()
            self.modular_content.append(Module.columnar_image_with_text(str(element), [image_id], caption, alignment))
        else:
            self.unhandled_elements.append("Embeded image has no ID")

    def _flush_collected_paragraphs_to_module(self):
        if self.paragraph_collector:
            paragraphs = "".join(self.paragraph_collector)
            self.modular_content.append(Module.paragraph(paragraphs))
            self.paragraph_collector = []

    def _add_embed_module(self, element):
        embed_url = element.attrs.get('url')
        if embed_url:
            self.modular_content.append(Module.full_width_embed(embed_url))
        else:
            self.unhandled_elements.append("Embeded video URL Not found.")


def generate_columnar_images_list(image_ids):
    list = []
    for id in image_ids:
        list.append({"image": id})
    return list


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
    def columnar_image_with_text(content, image_ids, caption, align_image, height=DEFAULT_HEIGHT):
        return {"type": "columnar_image_with_text",
                "value": {
                    "images": generate_columnar_images_list(image_ids),
                    "caption": caption,
                    "align_columnar_images": align_image,
                    "content": Module.rich_text(content),
                    "height": height,
                }
                }

    @staticmethod
    def full_width_embed(embed_url):
        return {
            "type": "full_width_embed",
            "value": {"embed": embed_url,
                      }
        }

    @staticmethod
    def image(image_id, caption):
        return {
            "caption": caption,
            "image": image_id
        }

    @staticmethod
    def rich_text(content):
        return {"content": content,
                "align_content": "default",
                }


if __name__ == '__main__':
    for article in Article.objects.live().all():
        print article.page_ptr_id, article,
        article_ = ArticleMigrator(article).formulate_modular_content().save_revision()
        print  article_.unhandled_elements
