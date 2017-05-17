from functional_tests.base import Test
from functional_tests.pages import AuthorPage

class TestAuthorPage(Test):
    author_page = None

    def setUp(self):
        page_lambda = lambda : AuthorPage(self.driver, '/authors/sasikumar-vasudevan/')
        self.__class__.author_page = self.load_page_if_not_loaded(self.author_page, page_lambda)

    def test_author_page_title(self):
        assert self.author_page.title == "All stories by V. Sasikumar"

    def test_author_info(self):
        assert self.author_page.author_name() == "V. Sasikumar"
