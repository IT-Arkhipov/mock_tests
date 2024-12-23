import requests
from requests import Response
from urllib.parse import urljoin
from fake_useragent import UserAgent

from utils.init import settings

ua = UserAgent()
headers = {'User-Agent': ua.random}


def get(endpoint: str, _headers=None, params=None) -> Response:
    if _headers is not None:
        headers.update(_headers)
    url = urljoin(settings.base_url, endpoint)
    response = requests.get(url=url, headers=headers, params=params)
    return response


def post(endpoint: str, _headers=None, params=None, body=None) -> Response:
    if _headers is not None:
        headers.update(_headers)
    url = urljoin(settings.base_url, endpoint)
    response = requests.post(url=url, headers=headers, params=params, json=body)
    return response
