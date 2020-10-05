import unittest
from converter import Converter


class TestConverter(unittest.TestCase):

    def setUp(self):
        self.converter = Converter()

    def test_dict_to_str(self):
        input_data = {
            "h1": "Title 1",
            "p": "Body 1"
        }
        result = self.converter.dict_to_str(input_data)
        self.assertEqual(result, '<h1>Title 1</h1><p>Body 1</p>')


if __name__ == "__main__":
    unittest.main()