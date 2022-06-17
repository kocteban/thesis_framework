""" Usage: (inside tests) =>  self.set_time_limit(SECONDS)
    Usage: (command-line) =>  --time-limit=SECONDS """

import pytest
from seleniumbase import BaseCase


class TimeLimitTests(BaseCase):
    @pytest.mark.expected_failure
    def test_time_limit_feature(self):
        self.set_time_limit(5)
        self.open("https://xkcd.com/1658/")
        print("\n(This test should fail)")
        self.sleep(7)
