from parameterized import parameterized
from seleniumbase import BaseCase


class GoogleTests(BaseCase):
    @parameterized.expand(
        [
            ["PyPI", "pypi.org", 'img[alt="PyPI"]'],
            ["Wikipedia", "www.wikipedia.org", "img.central-featured-logo"]
        ]
    )
    def test_parameterized_google_search(self, search_key, expected_text, img):
        self.open("https://google.com/ncr")
        self.type('input[title="Search"]', search_key + "\n")
        self.assert_text(expected_text, "#search")
        self.click('a:contains("%s")' % expected_text)
        self.assert_element(img)

