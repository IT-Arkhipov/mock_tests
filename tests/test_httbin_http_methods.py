from unittest.mock import patch, MagicMock
import unittest

import pytest

from resources.endpoints import endpoint
from utils import api_requests
from utils.init import settings


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
    @pytest.mark.mocked
    @pytest.mark.skipif(settings.skip_mocking, reason='Skipping mocking')
    @patch('utils.api_requests.requests')
    def test_mocked_get_method_response_code(self, request_mock):
        # ARRANGE
        expected_response_code = 200

        response_mock = MagicMock()
        response_mock.status_code = 200  # Set expected status code
        response_mock.json.return_value = {"key": "value"}  # Optionally set JSON response
        request_mock.get.return_value = response_mock

        # ACT
        response = api_requests.get(endpoint='test')
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
