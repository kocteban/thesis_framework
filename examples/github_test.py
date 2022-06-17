from seleniumbase import BaseCase


class GitHubTests(BaseCase):
    def test_github(self):
        if self.headless:
            self.open_if_not_url("about:blank")
            print("\n  This test is NOT designed for Headless Mode!")
            self.skip('Do NOT use "--headless" with this test!')
        self.open("https://github.com/search?q=muzofond_study")
        self.slow_click('a[href="/kocteban/Muzofond_Study"]')
        self.click_if_visible('[data-action="click:signup-prompt#dismiss"]')
        self.assert_element("div.repository-content")
        self.assert_text("Muzofond_Study", "h2 strong")
        self.slow_click('a[title="Muzofond"]')

