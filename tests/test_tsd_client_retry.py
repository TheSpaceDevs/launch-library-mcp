# tests/test_retry.py
import unittest
from launch_library_mcp.launch_library_client.retry import retry, throttle
from unittest.mock import MagicMock
import time


class TestRetry(unittest.TestCase):
    def test_retry_success(self):
        """@retryデコレーター 正常系"""
        successful_function_inner = MagicMock(return_value="Success")

        @retry(max_retry=3, retry_interval=0.1)
        def successful_function():
            return successful_function_inner()

        result = successful_function()
        self.assertEqual(result, "Success")
        successful_function_inner.assert_called_once()

    def test_retry_fail(self):
        """@retryデコレーター 異常系"""
        failing_function_inner = MagicMock(side_effect=ValueError("Failure"))

        @retry(max_retry=3, retry_interval=0.1)
        def failing_function():
            return failing_function_inner()

        with self.assertRaises(Exception) as context:
            failing_function()
            self.assertTrue("ValueError" in str(context.exception))
            self.assertEqual(failing_function_inner.call_count, 3)

    def test_retry_retry_on(self):
        """@retryデコレーター retry_on"""
        failing_function_inner = MagicMock(
            side_effect=[ValueError("Failure"), "Success"]
        )

        @retry(
            max_retry=3,
            retry_interval=0.1,
            retry_on=lambda e: isinstance(e, ValueError),
        )
        def failing_function():
            """ValueErrorが発生したらリトライする"""
            return failing_function_inner()

        result = failing_function()
        self.assertEqual(result, "Success")
        self.assertEqual(failing_function_inner.call_count, 2)

    def test_retry_retry_on_other_exception(self):
        """@retryデコレーター retry_on 指定の例外以外が発生したらそのままraiseする"""
        failing_function_inner = MagicMock(side_effect=Exception("Failure"))

        @retry(
            max_retry=3,
            retry_interval=0.1,
            retry_on=lambda e: isinstance(e, ValueError),
        )
        def failing_function():
            """Exceptionが発生してもリトライしない"""
            return failing_function_inner()

        with self.assertRaises(Exception):
            failing_function()

        self.assertEqual(failing_function_inner.call_count, 1)

    def test_retry_retry_on_exception(self):
        """@retryデコレーター retry_on_exception"""
        failing_function_inner = MagicMock(side_effect=ValueError("Failure"))

        @retry(
            max_retry=3,
            retry_interval=0.1,
            retry_on_exception=lambda e: isinstance(e, ValueError),
        )
        def failing_function():
            """ValueErrorが発生してもリトライしない"""
            return failing_function_inner()

        with self.assertRaises(ValueError):
            failing_function()

        self.assertEqual(failing_function_inner.call_count, 1)

    def test_retry_retry_on_exception_other_exception(self):
        """@retryデコレーター retry_on_exception 指定の例外以外が発生したらそのままリトライする"""
        failing_function_inner = MagicMock(
            side_effect=[Exception("Failure"), "Success"]
        )

        @retry(
            max_retry=3,
            retry_interval=0.1,
            retry_on_exception=lambda e: isinstance(e, ValueError),
        )
        def failing_function():
            """ValueErrorが発生してもリトライしない = それ以外の例外はリトライする"""
            return failing_function_inner()

        result = failing_function()
        self.assertEqual(result, "Success")
        self.assertEqual(failing_function_inner.call_count, 2)

class TestRetryAsync(unittest.IsolatedAsyncioTestCase):
    async def test_retry_success(self):
        successful_function_inner = MagicMock(return_value="Success")

        @retry(max_retry=3, retry_interval=0.1)
        async def async_successful_function():
            return successful_function_inner()

        result = await async_successful_function()
        self.assertEqual(result, "Success")
        successful_function_inner.assert_called_once()

    async def test_retry_fail(self):
        failing_function_inner = MagicMock(side_effect=ValueError("Failure"))

        @retry(max_retry=3, retry_interval=0.1)
        async def async_failing_function():
            return failing_function_inner()

        with self.assertRaises(Exception) as context:
            await async_failing_function()

        self.assertTrue("Failure" in str(context.exception))
        self.assertEqual(failing_function_inner.call_count, 3)

class TestThrottle(unittest.TestCase):
    def test_throttle_sync(self):
        """throttleデコレーター 同期関数のテスト"""
        call_times = []

        @throttle(min_interval=0.5)
        def test_function():
            call_times.append(time.time())
            return "success"

        # First call should execute immediately
        result1 = test_function()
        # Second call should be throttled
        result2 = test_function()
        # Third call should be throttled
        result3 = test_function()

        self.assertEqual(result1, "success")
        self.assertEqual(result2, "success")
        self.assertEqual(result3, "success")

        # Check that calls were properly spaced
        self.assertGreaterEqual(call_times[1] - call_times[0], 0.5)
        self.assertGreaterEqual(call_times[2] - call_times[1], 0.5)


class TestThrottleAsync(unittest.IsolatedAsyncioTestCase):
    async def test_throttle_async(self):
        """throttleデコレーター 非同期関数のテスト"""
        call_times = []

        @throttle(min_interval=0.5)
        async def test_function():
            call_times.append(time.time())
            return "success"

        # First call should execute immediately
        result1 = await test_function()
        # Second call should be throttled
        result2 = await test_function()
        # Third call should be throttled
        result3 = await test_function()

        self.assertEqual(result1, "success")
        self.assertEqual(result2, "success")
        self.assertEqual(result3, "success")

        # Check that calls were properly spaced
        self.assertGreaterEqual(call_times[1] - call_times[0], 0.5)
        self.assertGreaterEqual(call_times[2] - call_times[1], 0.5)

    async def test_throttle_preserves_exception(self):
        """throttleデコレーター 例外が保持されることを確認"""

        @throttle(min_interval=0.2)
        async def failing_function():
            raise ValueError("Test exception")

        with self.assertRaises(ValueError) as context:
            await failing_function()

        self.assertEqual(str(context.exception), "Test exception")


if __name__ == "__main__":
    unittest.main()
