from unittest.mock import patch, MagicMock
import unittest

from resources.endpoints import endpoint
from utils import api_requests


class TestGetMethods(unittest.TestCase):
    endpoint = endpoint.get

    def test_get_method_response_code(self):
        # ARRANGE
        expected_response_code = 200
        # ACT
        response = api_requests.get(self.endpoint)
        # ASSERT
        self.assertEqual(
            response.status_code, expected_response_code, msg=f'Wrong response code: {response.status_code}'
        )

    # mocked response test
    @patch('utils.api_requests.requests')
    def test_mocked_get_method_response_code(self, requests_mock):
        # ARRANGE
        response_mock = MagicMock()
        response_mock.status_code = 200
        requests_mock.get.return_value = response_mock

        _endpoint = ''
        expected_response_code = 200
        # ACT
        response = api_requests.get(_endpoint)
        # ASSERT
        self.assertEqual(
            response.status_code, expected_response_code, msg=f'Wrong response code: {response.status_code}'
        )

    class TestPostMethods(unittest.TestCase):
        endpoint = endpoint.post

        def test_post_method_response_code(self):
            # ARRANGE
            expected_response_code = 200
            # ACT
            response = api_requests.post(self.endpoint)
            # ASSERT
            self.assertEqual(
                response.status_code, expected_response_code, msg=f'Wrong response code: {response.status_code}'
            )
