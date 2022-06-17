from seleniumbase import BaseCase


class YouTubeSearchTests(BaseCase):
    def test_youtube_autocomplete_results(self):
        """Verify YouTube autocomplete search results."""
        self.open("https://www.youtube.com/")
        search_term = "cats"
        search_selector = "input#search"
        result_selector = 'li[role="presentation"]'

        self.click_if_visible('button[aria-label="Close"]')
        self.double_click(search_selector)
        self.type(search_selector, search_term)

        self.assert_element(result_selector)
        top_result = self.get_text(result_selector)

        self.assert_true(
            search_term in top_result,
            'Expected text "%s" not found in top result! '
            'Actual text was "%s"!' % (search_term, top_result),
        )
        self.click(result_selector)
        self.assert_element_present('a[aria-label*="Kittens"]')
