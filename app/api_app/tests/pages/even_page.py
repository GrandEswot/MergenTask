import requests


class EvenPage:
    def __init__(self):
        self.link = 'http://127.0.0.1:8000/even'

    def get_status_code(self):
        result = requests.get(self.link)
        assert 200 == result.status_code, 'status code should be OK 200'

    def check_method_get(self, parameters):
        result = requests.get(self.link, params=parameters)
        assertion_result = result.json()['result']
        assert assertion_result == True

    def check_method_post(self, parameters):
        result = requests.post(self.link, params=parameters)
        print(result.json()['result'])
        assert all([i % 2 == 0 for i in result.json()['result']]) == True


class OddPage(EvenPage):
    def __init__(self):
        super().__init__()
        self.link = 'http://127.0.0.1:8000/odd'

    def check_method_post(self, parameters):
        result = requests.post(self.link, params=parameters)
        print(result.json()['result'])
        assert all([i % 2 != 0 for i in result.json()['result']]) == True
