from functional_tests.base import Test
from functional_tests.pages import AuthorPage

class TestAuthorPage(Test):

    def test_author_page_title(self):
        author_page = AuthorPage(self.driver, '/authors/sasikumar-vasudevan/').open().wait_for_loading()
        assert author_page.title == "All stories by V. Sasikumar"
