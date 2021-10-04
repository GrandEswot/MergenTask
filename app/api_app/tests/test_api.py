import time
import pytest

from pages.even_page import EvenPage, OddPage


class TestAPIMethodGetForEvenPage:
    def test_check_status_code_for_method_get(self):
        even_page = EvenPage()
        even_page.get_status_code()

    @pytest.mark.parametrize('parameters',
                             [
                                 {'number': '22'},
                                 pytest.param({'number': '1, 2, 3'}, marks=pytest.mark.xfail),
                                 {'number': '0'},
                                 pytest.param({'number': ''}, marks=pytest.mark.xfail),
                                 {'number': '-2'},
                                 pytest.param({'number': 'строка'}, marks=pytest.mark.xfail),
                                 {'number': '-2, -4, 6'}
                             ]
                             )
    def test_method_get_for_even_numbers(self, parameters):
        even_page = EvenPage()
        even_page.check_method_get(parameters)

    @pytest.mark.parametrize('parameters',
                             [
                                 {'numbers': '22'},
                                 {'numbers': '1, 2, 3'},
                                 {'numbers': '0'},
                                 pytest.param({'numbers': ''}, marks=pytest.mark.xfail),
                                 {'numbers': '-3'},
                                 pytest.param({'numbers': 'строка'}, marks=pytest.mark.xfail),
                                 {'numbers': '-2, -4, 6'}
                             ]
                             )
    def test_method_post_for_even_number(self, parameters):
        even_page = EvenPage()
        even_page.check_method_post(parameters)


class TestAPIMethodGetForOddPage:
    def test_check_status_code_for_method_get(self):
        odd_page = OddPage()
        odd_page.get_status_code()

    @pytest.mark.parametrize('parameters',
                             [
                                 {'number': '11'},
                                 pytest.param({'number': '1, 2, 3'}, marks=pytest.mark.xfail),
                                 pytest.param({'number': '0'}, marks=pytest.mark.xfail),
                                 pytest.param({'number': ''}, marks=pytest.mark.xfail),
                                 {'number': '-3'},
                                 pytest.param({'number': 'строка'}, marks=pytest.mark.xfail),
                                 {'number': '-3, -5, 7'}
                             ]
                             )
    def test_method_get_for_odd_numbers(self, parameters):
        odd_page = OddPage()
        odd_page.check_method_get(parameters)

    @pytest.mark.parametrize('parameters',
                             [
                                 {'numbers': '11'},
                                 {'numbers': '1, 2, 3'},
                                 {'numbers': '0'},
                                 pytest.param({'numbers': ''}, marks=pytest.mark.xfail),
                                 {'numbers': '-3'},
                                 pytest.param({'numbers': 'строка'}, marks=pytest.mark.xfail),
                                 {'numbers': '-3, -5, 7'}
                             ]
                             )
    def test_method_post_for_even_number(self, parameters):
        odd_page = OddPage()
        odd_page.check_method_post(parameters)
