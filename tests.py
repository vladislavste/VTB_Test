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

    def test_list_creator(self):
        input_data = [
            {
                "h1": "Title 1",
                "p": "Body 1"
            },
            {
                "h1": "Title 2",
                "p": "Body 2"
            }
        ]
        result = self.converter.html_list_creator(input_data)
        self.assertEqual(result,
                         '<ul><li><h1>Title 1</h1><p>Body 1</p></li><li><h1>Title 2</h1><p>Body 2</p></li></ul>')


if __name__ == "__main__":
    unittest.main()
