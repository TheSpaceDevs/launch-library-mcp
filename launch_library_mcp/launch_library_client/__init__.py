# launch_library_client/__init__.py
import logging
import time
from requests.exceptions import HTTPError

import launch_library_mcp.launch_library_client.ll2.client as ll2_client
import launch_library_mcp.launch_library_client.sfn.client as sfn_client
from launch_library_mcp.launch_library_client.retry import throttle, retry
from launch_library_mcp.launch_library_client.api_client import detect_retryable_status

logger = logging.getLogger(__name__)

SNAPI_THROTTLE = 15
RETRYABLE_STATUS = [504, 524]
LLV2_BASE_URL = "https://ll.thespacedevs.com/"
SACEFLIGHT_NEWS_BASE_URL = "https://api.spaceflightnewsapi.net/"


class LaunchLibClient(ll2_client.LaunchLibrary2DocsClient):
    def __init__(
        self,
        base_url=LLV2_BASE_URL,
        api_key=None,
        default_headers=None,
        **kwargs,
    ):
        if api_key:
            default_headers = {
                **(default_headers or {}),
                "Authorization": f"Token {api_key}",
            }
        super().__init__(base_url=base_url, default_headers=default_headers, **kwargs)

    @retry(
        max_retry=5,
        retry_interval=SNAPI_THROTTLE,
        retry_on=detect_retryable_status(retry_status=RETRYABLE_STATUS),
    )
    def _callApiReq(
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
        try:
            return super()._callApiReq(
                method, path, data, headers, cookies, query, files, auth=auth
            )
        except HTTPError as e:
            # 429エラーの場合は、APIのスロットリングを考慮してリトライする
            if e.response.status_code == 429:
                logger.warning("Rate limit exceeded. Retrying...")
                throttle = self.api_throttle_list()
                logger.info(f"Next use: {throttle.next_use_secs + 1} seconds")
                time.sleep(throttle.next_use_secs + 1)
                return super()._callApiReq(
                    method, path, data, headers, cookies, query, files
                )
            raise e


class SpaceflightNewsApiClient(sfn_client.SpaceflightNewsApiClient):
    def __init__(self, base_url=SACEFLIGHT_NEWS_BASE_URL, **kwargs):
        super().__init__(base_url=base_url, **kwargs)

    @retry(
        max_retry=5,
        retry_interval=SNAPI_THROTTLE,
        retry_on=detect_retryable_status(retry_status=RETRYABLE_STATUS),
    )
    @throttle(min_interval=5)
    def _callApiReq(
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
        try:
            return super()._callApiReq(
                method, path, data, headers, cookies, query, files, auth=auth
            )
        except HTTPError as e:
            # 429エラーの場合は、APIのスロットリングを考慮してリトライする
            if e.response.status_code == 429:
                logger.warning("Rate limit exceeded. Retrying...")
                logger.info(f"Next use: {SNAPI_THROTTLE + 1} seconds")
                time.sleep(SNAPI_THROTTLE + 1)
                return super()._callApiReq(
                    method, path, data, headers, cookies, query, files, auth=auth
                )
            raise e
