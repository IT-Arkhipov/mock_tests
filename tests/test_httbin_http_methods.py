from unittest.mock import patch
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
