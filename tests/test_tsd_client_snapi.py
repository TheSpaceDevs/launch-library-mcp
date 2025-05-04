# tests/test_models.py
import unittest

import launch_library_mcp.launch_library_client.sfn.models as models
from launch_library_mcp.launch_library_client import SpaceflightNewsApiClient


class TestNewsClient(unittest.TestCase):
    def test_import_models(self):
        models.Article()

    def test_news_client(self):
        req = SpaceflightNewsApiClient()
        id = "d1b5f507-66a9-450a-86ac-b7b86c34eee4"
        res = req.articles_list(launch=id)
        self.assertIn(id, [x.launch_id for x in res.results[0].launches])


if __name__ == "__main__":
    unittest.main()
