import unittest
from unittest.mock import patch, MagicMock
from requests.exceptions import HTTPError
from launch_library_mcp.launch_library_client import LaunchLibClient
from launch_library_mcp.launch_library_client import (
    SpaceflightNewsApiClient,
    SNAPI_THROTTLE,
)


class TestLaunchLibClient(unittest.TestCase):
    @patch(
        "launch_library_mcp.launch_library_client.ll2.client.LaunchLibrary2DocsClient._callApiReq"
    )
    def test_call_api_req_with_success(self, mock_super_call):
        mock_super_call.return_value = {"status": "success"}

        client = LaunchLibClient()

        response = client._callApiReq("GET", "/test-path")

        mock_super_call.assert_called_once_with(
            "GET", "/test-path", None, None, None, None, None, auth=None
        )
        self.assertEqual(response, {"status": "success"})

    @patch("time.sleep", return_value=None)  # time.sleep をモックしてテストを高速化
    @patch(
        "launch_library_mcp.launch_library_client.ll2.client.LaunchLibrary2DocsClient._callApiReq"
    )
    def test_call_api_req_with_retry_on_429(self, mock_super_call, mock_sleep):
        error_response = MagicMock()
        error_response.status_code = 429
        mock_super_call.side_effect = [
            HTTPError(response=error_response),
            {"status": "success"},
        ]

        # api_throttle_list のモック
        mock_throttle = MagicMock()
        mock_throttle.next_use_secs = 1

        with patch.object(
            LaunchLibClient, "api_throttle_list", return_value=mock_throttle
        ):
            client = LaunchLibClient()

            response = client._callApiReq("GET", "/test-path")

            self.assertEqual(response, {"status": "success"})
            self.assertEqual(mock_super_call.call_count, 2)
            mock_sleep.assert_called_once_with(2)

    @patch(
        "launch_library_mcp.launch_library_client.ll2.client.LaunchLibrary2DocsClient._callApiReq"
    )
    def test_call_api_req_with_other_http_error(self, mock_super_call):
        error_response = MagicMock()
        error_response.status_code = 500
        mock_super_call.side_effect = HTTPError(response=error_response)

        client = LaunchLibClient()

        with self.assertRaises(HTTPError):
            client._callApiReq("GET", "/test-path")
        mock_super_call.assert_called_once_with(
            "GET", "/test-path", None, None, None, None, None, auth=None
        )


class TestSpaceflightNewsApiClient(unittest.TestCase):
    @patch(
        "launch_library_mcp.launch_library_client.sfn.client.SpaceflightNewsApiClient._callApiReq"
    )
    def test_call_api_req_with_success(self, mock_super_call):
        mock_super_call.return_value = {"status": "success"}

        client = SpaceflightNewsApiClient()

        response = client._callApiReq("GET", "/articles")

        mock_super_call.assert_called_once_with(
            "GET", "/articles", None, None, None, None, None, auth=None
        )
        self.assertEqual(response, {"status": "success"})

    @patch("time.sleep", return_value=None)
    @patch(
        "launch_library_mcp.launch_library_client.sfn.client.SpaceflightNewsApiClient._callApiReq"
    )
    def test_call_api_req_with_retry_on_429(self, mock_super_call, mock_sleep):
        # Mock a 429 error followed by a success
        error_response = MagicMock()
        error_response.status_code = 429
        mock_super_call.side_effect = [
            HTTPError(response=error_response),  # First call fails
            {"status": "success"},  # Retry succeeds
        ]

        client = SpaceflightNewsApiClient()

        # Execute
        response = client._callApiReq("GET", "/articles")

        # Assert
        self.assertEqual(mock_super_call.call_count, 2)  # Called twice
        self.assertEqual(response, {"status": "success"})
        mock_sleep.assert_called_once_with(
            SNAPI_THROTTLE + 1
        )  # Sleeps for SNAPI_THROTTLE + 1 seconds

    @patch(
        "launch_library_mcp.launch_library_client.sfn.client.SpaceflightNewsApiClient._callApiReq"
    )
    def test_call_api_req_with_other_http_error(self, mock_super_call):
        # Mock a 500 error
        error_response = MagicMock()
        error_response.status_code = 500
        mock_super_call.side_effect = HTTPError(response=error_response)

        client = SpaceflightNewsApiClient()

        # Execute & Assert
        with self.assertRaises(HTTPError):
            client._callApiReq("GET", "/articles")

        mock_super_call.assert_called_once_with(
            "GET", "/articles", None, None, None, None, None, auth=None
        )


if __name__ == "__main__":
    unittest.main()
