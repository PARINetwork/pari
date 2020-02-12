import json

from article.models import Article, ArticleAuthors
from functional_tests.base import Test
from functional_tests.data_setup import DataSetup
from functional_tests.factory import AuthorFactory, CategoryFactory, LocationFactory, ImageFactory
from functional_tests.pages import ArticlePage


def get_modular_content(article_id,image_id,location_id):
    return [{
                "type": "paragraph",
                "value": {
                    "content": "<p>A test that make test</p>",
                    "align_content": "default"
                }

            }, {
            "type": "n_column_paragraph",
            "value": {
                "paragraph": [{
                    "content": "<p>A test that make test</p>",
                    "align_content": "default"
                }]
            }
            }, {
            "type": "paragraph_with_map",
            "value": {
                "content": {
                    "content": "<p>A test that make test</p>",
                    "align_content": "default"
                },
                "map_align": "left",
                "locations": [location_id]
            }
            }, {
            "type": "paragraph_with_page",
            "value": {
                "content": {
                    "content": "<p>A test that make test</p>",
                    "align_content": "default"
                },
                "align_image": "left",
                "page": article_id
            }
            }, {
            "type": "paragraph_with_quote",
            "value": {
                "content": {
                    "content": "<p>A test that make test</p>",
                    "align_content": "default"
                },
                "quote": "<p>\"A test that make test\"</p>",
                "align_quote": "right"
            }
            }, {
            "type": "full_width_quote",
            "value": {
                "quote": "<p><b>\"A test that make test\"</b></p>"
            }
            }, {
            "type": "video_with_quote",
            "value": {
                "video_height": 270,
                "quote": "<p><b>\"A test that make test\"</b><br/></p>",
                "video": "https://www.youtube.com/watch?v=oKjfRr_D-HA",
                "align_quote": "left",
                "video_caption": "<p>A test that make test<br/></p>"
            }
            }, {
            "type": "image_with_quote_and_paragraph",
            "value": {
                "quote": {
                    "quote": "<p><b>A test that make test</b></p>"
                },
                "image": {
                    "caption": "<p>A test that make test</p>",
                    "image": image_id,
                    "height": 380
                },
                "align_image": "left",
                "content_1": {
                    "content": "<p>A test that make test</p>",
                    "align_content": "default"
                },
                "content_2": {
                    "content": "<p>A test that make test</p>",
                    "align_content": "default"
                }
            }
            }, {
            "type": "full_width_image",
            "value": {
                "caption": "",
                "image": {
                    "image": image_id
                }
            }
            }, {
            "type": "columnar_image_with_text",
            "value": {
                "images": [{
                    "image": image_id
                }, {
                    "image": image_id
                }],
                "caption": "<p>A test that make test</p>",
                "align_columnar_images": "left",
                "content": {
                    "content": "<p>A test that make test</p>",
                    "align_content": "default"
                },
                "height": 380
            }
            }, {
            "type": "full_width_embed",
            "value": {
                "embed": "https://www.youtube.com/watch?v=oKjfRr_D-HA",
                "embed_caption": "<p>A test that make test</p>"
            }
            }, {
            "type": "paragraph_with_embed",
            "value": {
                "content": {
                    "content": "<p>A test that make test</p>",
                    "align_content": "default"
                },
                "embed": "https://www.youtube.com/watch?v=oKjfRr_D-HA",
                "embed_max_width": 200,
                "embed_caption": "<p>A test that make test</p>",
                "embed_align": "left"
            }
            }, {
            "type": "paragraph_with_raw_embed",
            "value": {
                "content": {
                    "content": "<p>a bad test</p>",
                    "align_content": "default"
                },
                "embed": "<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/oKjfRr_D-HA\" frameborder=\"0\" allowfullscreen></iframe>",
                "embed_caption": "",
                "embed_align": "left"
            }
            }]

class TestArticlePage(Test):
    article_page = None

    def setUp(self):
        page_lambda = lambda: ArticlePage(self.driver, '/articles/article-page/')
        self.__class__.article_page = self.load_page_if_not_loaded(self.article_page, page_lambda)

    @classmethod
    def setUpClass(cls):
        super(TestArticlePage, cls).setUpClass()
        author = AuthorFactory.create(name="Nimesh", slug="puli")
        article_author = ArticleAuthors(author=author, sort_order=0)
        category = CategoryFactory.create(name="Adivasis", slug="adivasis", order=2, description="The first dwellers")
        location = LocationFactory.create(name="Madurai", slug="madurai")
        image = ImageFactory.create(photographers=(author,), locations=(location,))
        setup = DataSetup()
        dummy_article = setup.create_article("Dummy", article_author, category, location, image)
        modular_article = setup.create_article("Article Page", article_author, category, location, image,
                                               show_modular_content=True, modular_content=json.dumps(get_modular_content(dummy_article.id,image.id,location.id)))

    def test_article_page_title(self):
        article_banner = self.article_page.banner_section()
        assert article_banner.title_of_the_article() == "Article Page"

    def test_article_paragraph_module_should_contain_expected_text(self):
        article_modular_content = self.article_page.modular_content()
        assert article_modular_content.paragraph_module_text() == 'A test that make test'

    def test_article_columnar_paragraph_module_should_contain_expected_text(self):
        article_modular_content = self.article_page.modular_content()
        assert article_modular_content.columnar_paragraph_module_text() == 'A test that make test'
