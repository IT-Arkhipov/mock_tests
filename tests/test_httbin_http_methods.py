from unittest.mock import patch, MagicMock
import unittest

import pytest

from resources.endpoints import endpoint
from utils import api_requests
from utils.init import settings


@pytest.fixture
def mock_requests_get():
    with patch('utils.api_requests.requests.get') as mock_get:
        # Create a mock response object
        response_mock = MagicMock()
        response_mock.status_code = 200  # Set expected status code
        response_mock.json.return_value = {"key": "value"}  # Optionally set JSON response

        # Configure the mock to return this response when called
        mock_get.return_value = response_mock
        yield mock_get  # Yield the mock for use in tests


@pytest.fixture
def mock_requests_post():
    with patch('utils.api_requests.requests.post') as mock_post:
        response_mock = MagicMock()
        response_mock.status_code = 201
        response_mock.json.return_value = {"message": "created"}
        mock_post.return_value = response_mock
        yield mock_post


@pytest.fixture(scope='function')
def mock_fixture(request):
    """Dynamically select which mock to use based on the test name."""
    if 'get' in request.node.name:
        return request.getfixturevalue('mock_requests_get')
    elif 'post' in request.node.name:
        return request.getfixturevalue('mock_requests_post')
    else:
        return None  # or raise an error if appropriate


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
    @pytest.mark.skipif(settings.skip_mocking, reason='Skipping mocking')
    @pytest.mark.usefixtures('mock_fixture')
    def test_mocked_get_method_response_code(self):
        # ARRANGE
        expected_response_code = 200
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
