import requests
import logging
from pydantic import BaseModel
from typing import Union, Dict, Tuple, Any
import urllib.parse
import asyncio
import json
from enum import Enum

from .retry import retry

logger = logging.getLogger(__name__)


class QueryType(Enum):
    """Enum for query types"""

    EQ = "EQUAL"
    N_EQ = "NOT_EQUAL"
    IN = "IN"
    BETWEEN = "BETWEEN"
    CONTAINS = "CONTAINS"
    GT = "GREATER_THAN"
    GT_E = "GREATER_THAN_OR_EQUAL"
    LT = "LESS_THAN"
    LT_E = "LESS_THAN_OR_EQUAL"
    BEGINS = "BEGINS_WITH"
    EX = "EXISTS"
    N_EX = "NOT_EXISTS"


def parse_params_query(value: Any = None, mode: QueryType = QueryType.EQ) -> str:
    if mode == QueryType.BETWEEN:
        if not isinstance(value, list):
            raise ValueError("value must be a list for BETWEEN mode")
        if len(value) != 2:
            raise ValueError("value must contain 2 elements for BETWEEN mode")
    func_mapping = {
        QueryType.LT_E: lambda v: f"...{v}",
        QueryType.LT: lambda v: f"..{v}",
        QueryType.GT_E: lambda v: f"{v}...",
        QueryType.GT: lambda v: f"{v}..",
        QueryType.BETWEEN: lambda v: f"{v[0]}...{v[1]}",
        QueryType.EX: lambda v: "*",
        QueryType.CONTAINS: lambda v: f"*{v}*",
        QueryType.BEGINS: lambda v: f"{v}*",
        QueryType.N_EX: lambda v: "--",
        QueryType.N_EQ: lambda v: f"--{v}",
        QueryType.EQ: lambda v: str(v),
    }
    func = func_mapping.get(mode, lambda v: str(v))
    return func(value)


def parse_params(params: Dict[str, Tuple[Any, QueryType]]) -> Dict[str, str]:
    res = {}
    for k, (v, mode) in params.items():
        res[k] = parse_params_query(v, mode)
    return res


# リトライ可能なステータスコード
# 冪等性があるもののみリトライする。バックエンドサーバーまでパケットが到達しているもの以外はリトライしない
DEFAULT_RETRYABLE_STATUS = [
    502,  # Bad Gateway: ゲートウェイが上流サーバーから不正な応答を受け取った場合
    503,  # Service Unavailable: サーバーが一時的に利用不可（過負荷やメンテナンス中）である場合
    504,  # Gateway Timeout: ゲートウェイが上流サーバーからの応答を待つ間にタイムアウトした場合
    429,  # Too Many Requests: クライアントからのリクエストが多すぎるため、レート制限が発動された場合
    408,  # Request Timeout: クライアントがリクエストを完了する前にタイムアウトした場合
    499,  # Client Closed Request: クライアントがリクエストを閉じた場合
    525,  # SSL Handshake Failed: SSLハンドシェイクに失敗した場合（通常、Cloudflare環境で発生）
    526,  # Invalid SSL Certificate: SSL証明書の検証に失敗した場合
    527,  # Railgun Error: Cloudflare固有のエラー。Railgunプロトコルに関連するエラーが発生した場合
]


def detect_retryable_status(retry_status=None):
    """HTTPステータスコード別でリトライ可能なエラーかどうかを判定する関数の生成"""
    return lambda e: any(
        str(status) in str(e)
        for status in set(retry_status) | set(DEFAULT_RETRYABLE_STATUS)
    )


def detect_retryable_error(e):
    """リトライ可能なエラーかどうかを判定する関数の生成"""
    if isinstance(
        e, (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout)
    ):
        return True
    if (
        isinstance(e, requests.exceptions.HTTPError)
        and e.response.status_code in DEFAULT_RETRYABLE_STATUS
    ):
        return True
    return False


def to_request_body(data):
    if isinstance(data, BaseModel):
        return data.model_dump_json()
    if isinstance(data, list):
        data = [
            json.loads(d.model_dump_json()) if isinstance(d, BaseModel) else d
            for d in data
        ]

    # JSON または文字列に変換する
    if isinstance(data, dict) or isinstance(data, list):
        data = json.dumps(data, ensure_ascii=False)
    elif not isinstance(data, str) and data is not None:
        data = str(data)
    return data


class JsonApi:
    def __init__(
        self,
        base_url=None,
        api_key=None,
        timeout=None,
        default_headers=None,
        cookies=None,
        trail_slash=True,
        auth=None,
    ):
        self.BASE_URL = base_url
        self.API_KEY = api_key
        self.timeout = timeout
        self.cookies = cookies
        self.default_headers = {
            "x-api-key": self.API_KEY,
            "Content-Type": "application/json",
            **(default_headers or {}),
        }
        self.trail_slash = trail_slash
        self.auth = auth

    @retry(max_retry=5, retry_interval=5, retry_on=detect_retryable_error)
    def _callApiReq(
        self,
        method,
        path: str,
        data=None,
        headers=None,
        cookies=None,
        query=None,
        files=None,
        auth=None,
    ):
        if not headers:
            headers = self.default_headers

        if query:
            if self.trail_slash and not path.endswith("/"):
                path += "/"
            path += "?"
            for key, value in query.items():
                if value is not None:
                    path += f"{key}={urllib.parse.quote(str(value), safe='')}&"
            path = path[:-1]

        url = self.BASE_URL + path
        # "/" の重複を避ける
        if not self.BASE_URL.endswith("/") and not path.startswith("/"):
            url = self.BASE_URL + "/" + path
        elif self.BASE_URL.endswith("/") and path.startswith("/"):
            url = self.BASE_URL + path[1:]
        url = url.replace("//", "/").replace(":/", "://")

        # ヘッダーはデフォルトのものを使う
        headers = {**self.default_headers, **(headers or {})}

        logger.debug(f"Calling {method} {url}")

        response = requests.request(
            method,
            url,
            data=to_request_body(data),
            headers=headers,
            cookies=cookies,
            files=files,
            timeout=self.timeout,
            auth=auth or self.auth,
        )
        try:
            response.raise_for_status()
            self.cookies = response.cookies
            return response
        except requests.exceptions.HTTPError as e:
            logger.info(
                f"Error: status={response.status_code} response={response.text}"
            )
            raise e

    def _callApiText(
        self,
        method,
        path,
        data=None,
        headers=None,
        cookies=None,
        query=None,
        files=None,
        auth=None,
    ) -> Union[dict, list]:
        response = self._callApiReq(
            method=method,
            path=path,
            data=data,
            headers=headers,
            cookies=cookies,
            query=query,
            files=files,
            auth=auth,
        )
        return response.text

    def _callApi(
        self,
        method,
        path,
        data=None,
        headers=None,
        cookies=None,
        query=None,
        files=None,
        auth=None,
    ) -> Union[dict, list, str]:
        response = self._callApiReq(
            method=method,
            path=path,
            data=data,
            headers=headers,
            cookies=cookies,
            query=query,
            files=files,
            auth=auth,
        )
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            # JSON でない場合はテキストとして返す
            return response.text

    def call(
        self,
        method,
        path,
        data=None,
        headers=None,
        cookies=None,
        query=None,
        files=None,
        auth=None,
    ):
        return self._callApi(method, path, data, headers, cookies, query, files, auth)

    @retry(
        max_retry=5,
        retry_interval=5,
        retry_on=detect_retryable_status(retry_status=[504]),
    )
    def get(self, path, data=None, headers=None, cookies=None, query=None, auth=None):
        return self._callApi("get", path, data, headers, cookies, query, None, auth)

    def post(
        self,
        path,
        data=None,
        headers=None,
        cookies=None,
        query=None,
        files=None,
        auth=None,
    ):
        return self._callApi("post", path, data, headers, cookies, query, files, auth)

    def put(
        self,
        path,
        data=None,
        headers=None,
        cookies=None,
        query=None,
        files=None,
        auth=None,
    ):
        return self._callApi("put", path, data, headers, cookies, query, files, auth)

    def delete(
        self, path, data=None, headers=None, cookies=None, query=None, auth=None
    ):
        return self._callApi("delete", path, data, headers, cookies, query, None, auth)

    async def _callApiReqAsync(
        self,
        method,
        path,
        data=None,
        headers=None,
        cookies=None,
        query=None,
        files=None,
        auth=None,
    ):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None,
            self._callApiReq,
            method,
            path,
            data,
            headers,
            cookies,
            query,
            files,
            auth,
        )

    async def _callApiTextAsync(
        self,
        method,
        path,
        data=None,
        headers=None,
        cookies=None,
        query=None,
        files=None,
        auth=None,
    ):
        response = await self._callApiReqAsync(
            method=method,
            path=path,
            data=data,
            headers=headers,
            cookies=cookies,
            query=query,
            files=files,
            auth=auth,
        )
        return response.text

    async def _callApiAsync(
        self,
        method,
        path,
        data=None,
        headers=None,
        cookies=None,
        query=None,
        files=None,
        auth=None,
    ):
        response = await self._callApiReqAsync(
            method=method,
            path=path,
            data=data,
            headers=headers,
            cookies=cookies,
            query=query,
            files=files,
            auth=auth,
        )
        return response.json()

    async def getAsync(
        self, path, data=None, headers=None, cookies=None, query=None, auth=None
    ):
        return await self._callApiAsync(
            "get", path, data, headers, cookies, query, None, auth
        )

    async def postAsync(
        self,
        path,
        data=None,
        headers=None,
        cookies=None,
        query=None,
        files=None,
        auth=None,
    ):
        return await self._callApiAsync(
            "post", path, data, headers, cookies, query, files, auth
        )

    async def putAsync(
        self,
        path,
        data=None,
        headers=None,
        cookies=None,
        query=None,
        files=None,
        auth=None,
    ):
        return await self._callApiAsync(
            "put", path, data, headers, cookies, query, files, auth
        )

    async def deleteAsync(
        self, path, data=None, headers=None, cookies=None, query=None, auth=None
    ):
        return await self._callApiAsync(
            "delete", path, data, headers, cookies, query, None, auth
        )
