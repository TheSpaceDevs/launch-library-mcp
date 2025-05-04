# tests/test_models.py
import unittest

import launch_library_mcp.launch_library_client.ll2.models as models
import launch_library_mcp.launch_library_client.ll2.client as client
from launch_library_mcp.launch_library_client import LaunchLibClient


class TestCLI(unittest.TestCase):
    def test_import_models(self):
        models.ImageVariantType(id=1, name="test")

    def test_import_client(self):
        client.LaunchLibrary2DocsClient()

    def test_ll2_client(self):
        req = LaunchLibClient()
        id = "d1b5f507-66a9-450a-86ac-b7b86c34eee4"
        res = req.launches_retrieve(id=id)
        self.assertEqual(res.id, id)

        res = req.launches_list(search="Starlink Group 12-5")
        self.assertEqual(res.results[0].name, "Falcon 9 Block 5 | Starlink Group 12-5")


if __name__ == "__main__":
    unittest.main()
