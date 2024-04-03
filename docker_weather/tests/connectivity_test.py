import requests


URL = 'http://127.0.0.1:9090'


def test_weatherapp_reachable():
    assert requests.options(URL).ok
