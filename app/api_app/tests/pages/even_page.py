import pytest
import selenium
import requests


class EvenPage:
    def __init__(self, browser):
        self.browser = browser
        self.link = 'http://127.0.0.1:8000/even'

    def get_status_code(self):
        result = self.browser.get(self.link)

        assert 200 == result.status_code, 'status code should be OK 200'

    @pytest.mark.parametrize('params',
                             [
                                 pytest.param([1, 2, 3], marks=pytest.mark.xfail),
                                 pytest.param(0, marks=pytest.mark.xfail),
                                 pytest.param([], marks=pytest.mark.xfail),
                                 [2],
                                 pytest.param('строка', marks=pytest.mark.xfail),
                                 [-2, -4, 6]
                             ]
                             )
    def check_method_get_values(self, params):
        result = requests.get(self.link, params=params)

        assert result == True

