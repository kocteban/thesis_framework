""" Testing the @pytest.mark.xfail marker.
    https://docs.pytest.org/en/latest/skipping.html
"""

import pytest
from seleniumbase import BaseCase


class XFailTests(BaseCase):
    @pytest.mark.xfail
    def test_xfail(self):
        self.open("https://xkcd.com/376/")
        self.sleep(1)
        self.fail("There is a known bug here!")
