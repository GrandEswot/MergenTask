import time
import pytest

from pages.even_page import EvenPage


class TestAPIMethodGet:
    def test_check_status_code_for_method_get(self, browser):
        page = EvenPage(browser)
        page.get_status_code()

    def test_method_get_works(self, browser):
        page = EvenPage(browser)
        page.check_method_get_values(browser)
