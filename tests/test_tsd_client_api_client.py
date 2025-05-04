import unittest
import requests
from unittest.mock import patch, ANY, MagicMock
from typing import Optional
from pydantic import BaseModel
from enum import Enum

from launch_library_mcp.launch_library_client.api_client import (
    JsonApi,
    parse_params_query,
    parse_params,
    QueryType,
)


def make_mock_response(status_code=None, json_data=None):
    mock_res = requests.Response()
    mock_res.json = lambda: json_data
    mock_res.status_code = status_code
    return mock_res


class DummyJsonEnum(Enum):
    A = "A"
    B = "B"


class DummyJsonBody(BaseModel):
    name: str
    age: int
    type: Optional[DummyJsonEnum] = None


class TestJsonApi(unittest.TestCase):

    def test_parse_params_query(self):
        """parse_params_query 正常系のテスト"""
        self.assertEqual(parse_params_query(30, QueryType.GT), "30..")
        self.assertEqual(parse_params_query([50, 100], QueryType.BETWEEN), "50...100")
        self.assertEqual(parse_params_query(mode=QueryType.EX), "*")
        self.assertEqual(parse_params_query("John", QueryType.BEGINS), "John*")
        self.assertEqual(parse_params_query(None, QueryType.N_EX), "--")
        self.assertEqual(parse_params_query("John", QueryType.N_EQ), "--John")
        self.assertEqual(parse_params_query(30), "30")

    def test_parse_params_query_edge_cases(self):
        """parse_params_query エッジケースのテスト"""
        self.assertEqual(parse_params_query("", QueryType.EQ), "")
        self.assertEqual(parse_params_query("@#$%", QueryType.BEGINS), "@#$%*")
        with self.assertRaises(ValueError):
            parse_params_query([1, 2, 3], QueryType.BETWEEN)
        with self.assertRaises(ValueError):
            parse_params_query("", QueryType.BETWEEN)

    def test_parse_params(self):
        """parse_params 正常系のテスト"""
        params = {
            "age": (30, QueryType.GT),
            "name": ("John", QueryType.BEGINS),
            "status": (None, QueryType.EX),
            "score": ([50, 100], QueryType.BETWEEN),
        }
        res = parse_params(params)
        self.assertEqual(res["age"], "30..")
        self.assertEqual(res["name"], "John*")
        self.assertEqual(res["status"], "*")
        self.assertEqual(res["score"], "50...100")

    @patch("launch_library_mcp.launch_library_client.api_client.requests.request")
    def test_get(self, mock_get):
        """GetItem 正常系のテスト"""
        mock_get.return_value = make_mock_response(200, {"key": "value"})

        api = JsonApi("xxx")
        res = api.get(path="xxx_123")
        self.assertEqual(res, {"key": "value"})
        mock_get.assert_called_once_with(
            "get",
            "xxx/xxx_123",
            data=None,
            headers=ANY,
            cookies=ANY,
            files=ANY,
            timeout=ANY,
            auth=None,  # Add auth parameter to assertion
        )

    @patch("launch_library_mcp.launch_library_client.api_client.requests.request")
    def test_get_with_auth(self, mock_get):
        """GetItem with auth parameter test"""
        mock_get.return_value = make_mock_response(200, {"key": "value"})

        # Test with auth at constructor
        test_auth = ("username", "password")
        api = JsonApi("xxx", auth=test_auth)
        res = api.get(path="xxx_123")
        mock_get.assert_called_with(
            "get",
            "xxx/xxx_123",
            data=None,
            headers=ANY,
            cookies=ANY,
            files=ANY,
            timeout=ANY,
            auth=test_auth,  # Should use the instance auth
        )

        # Test with auth at method call
        method_auth = ("other_user", "other_pass")
        res = api.get(path="xxx_123", auth=method_auth)
        mock_get.assert_called_with(
            "get",
            "xxx/xxx_123",
            data=None,
            headers=ANY,
            cookies=ANY,
            files=ANY,
            timeout=ANY,
            auth=method_auth,  # Should use the method auth
        )
        self.assertEqual(res, {"key": "value"})

    @patch("launch_library_mcp.launch_library_client.api_client.requests.request")
    @patch("time.sleep")
    def test_get_retry(self, mock_sleep, mock_get):
        """GetItem リトライ可能なエラー"""
        mock_get.side_effect = [
            make_mock_response(502),  # リトライ可能なステータスコード
            make_mock_response(504),  # リトライ可能なステータスコード
            requests.exceptions.ConnectionError(),  # リトライ可能な例外
            make_mock_response(200, {"key": "value"}),
        ]
        api = JsonApi("xxx")
        res = api.get(path="xxx_123")
        self.assertEqual(res, {"key": "value"})
        self.assertEqual(mock_get.call_count, 4)

    @patch("launch_library_mcp.launch_library_client.api_client.requests.request")
    def test_post(self, mock_post):
        """PostItem 正常系のテスト"""
        mock_post.return_value = make_mock_response(200, {"key": "value"})

        api = JsonApi("xxx")
        res = api.post(
            path="xxx_123",
            data=DummyJsonBody(name="John", age=30, type=DummyJsonEnum.A),
        )
        self.assertEqual(res, {"key": "value"})
        mock_post.assert_called_once_with(
            "post",
            "xxx/xxx_123",
            data='{"name":"John","age":30,"type":"A"}',
            headers=ANY,
            cookies=ANY,
            files=ANY,
            timeout=ANY,
            auth=None,
        )

    @patch("launch_library_mcp.launch_library_client.api_client.requests.request")
    def test_put(self, mock_put):
        """PutItem 正常系のテスト"""
        mock_put.return_value = make_mock_response(200, {"key": "value"})

        api = JsonApi("xxx")
        res = api.put(path="xxx_123", data=[DummyJsonBody(name="名前", age=30)])
        self.assertEqual(res, {"key": "value"})
        mock_put.assert_called_once_with(
            "put",
            "xxx/xxx_123",
            data='[{"name": "名前", "age": 30, "type": null}]',
            headers=ANY,
            cookies=ANY,
            files=ANY,
            timeout=ANY,
            auth=None,
        )

    @patch("launch_library_mcp.launch_library_client.api_client.requests.request")
    def test_delete(self, mock_delete):
        """DeleteItem 正常系のテスト"""
        mock_res = requests.Response()
        mock_res.json = MagicMock(
            side_effect=requests.exceptions.JSONDecodeError(
                "Expecting value: line 1 column 1 (char 0)", "", 0
            )
        )
        mock_res.status_code = 200
        mock_res._content = "test response".encode("utf-8")
        mock_delete.return_value = mock_res

        api = JsonApi("xxx")
        res = api.delete(path="xxx_123")
        self.assertEqual(res, "test response")
        mock_delete.assert_called_once_with(
            "delete",
            "xxx/xxx_123",
            data=None,
            headers=ANY,
            cookies=ANY,
            files=ANY,
            timeout=ANY,
            auth=None,
        )

    @patch("launch_library_mcp.launch_library_client.api_client.requests.request")
    def test_delete_empty_response(self, mock_delete):
        """空のレスポンスのテスト"""
        mock_res = requests.Response()
        mock_res.status_code = 200
        mock_res._content = "".encode("utf-8")
        mock_delete.return_value = mock_res

        api = JsonApi("xxx")
        res = api.delete(path="xxx_123")
        self.assertEqual(res, "")


class TestJsonApiAsync(unittest.IsolatedAsyncioTestCase):

    @patch("launch_library_mcp.launch_library_client.api_client.requests.request")
    async def test_get(self, mock_get):
        """GetItem 正常系のテスト"""
        mock_res = make_mock_response(200, {"key": "value"})

        api = JsonApi("xxx")
        mock_get.return_value = mock_res
        res = await api.getAsync(path="xxx_123", query={"name": "John"})
        self.assertEqual(res, {"key": "value"})
        mock_get.assert_called_once_with(
            "get",
            "xxx/xxx_123/?name=John",
            data=None,
            headers=ANY,
            cookies=ANY,
            files=ANY,
            timeout=ANY,
            auth=None,
        )

    @patch("launch_library_mcp.launch_library_client.api_client.requests.request")
    async def test_post(self, mock_post):
        """PostItem 正常系のテスト"""
        mock_post.return_value = make_mock_response(200, {"key": "value"})

        api = JsonApi("xxx")
        res = await api.postAsync(
            path="xxx_123",
            data=DummyJsonBody(name="John", age=30, type=DummyJsonEnum.A),
        )
        self.assertEqual(res, {"key": "value"})
        mock_post.assert_called_once_with(
            "post",
            "xxx/xxx_123",
            data='{"name":"John","age":30,"type":"A"}',
            headers=ANY,
            cookies=ANY,
            files=ANY,
            timeout=ANY,
            auth=None,
        )

    @patch("launch_library_mcp.launch_library_client.api_client.requests.request")
    async def test_put(self, mock_put):
        """PutItem 正常系のテスト"""
        mock_put.return_value = make_mock_response(200, {"key": "value"})

        api = JsonApi("xxx", trail_slash=False)
        res = await api.putAsync(
            path="xxx_123",
            data=[DummyJsonBody(name="名前", age=30)],
            query={"name": "John"},
        )
        self.assertEqual(res, {"key": "value"})
        mock_put.assert_called_once_with(
            "put",
            "xxx/xxx_123?name=John",  # trail_slash=False でクエリパラメータが付与される
            data='[{"name": "名前", "age": 30, "type": null}]',
            headers=ANY,
            cookies=ANY,
            files=ANY,
            timeout=ANY,
            auth=None,
        )


if __name__ == "__main__":
    unittest.main()
