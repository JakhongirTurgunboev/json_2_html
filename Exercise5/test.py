import unittest

from main import json_converter


class TestConverter(unittest.TestCase):
    def test_converter(self):
        """
        Test that it return valid data
        """
        json_data = {
                      "p.my-class#my-id": "hello",
                      "p.my-class1.my-class2": "example<a>asd</a>"
                    }
        self.assertEqual(json_converter(json_data), "<p id=\"my-id\" class=\"my-class\">hello</p><p "
                                                    "class=\"my-class1 my-class2\">example&lt;a&gt;asd&lt;/a&gt;</p>")


if __name__ == '__main__':
    unittest.main()
