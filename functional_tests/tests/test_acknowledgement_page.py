from functional_tests.base import Test
from functional_tests.pages import AcknowledgementPage


class TestAcknowledgementPage(Test):
    def test_donate_page_title(self):
        acknowledgement_home = AcknowledgementPage(self.driver).open().wait_for_loading()

        assert acknowledgement_home.title == "Acknowledgements"
