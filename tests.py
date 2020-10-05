import unittest
from converter import Converter


class TestConverter(unittest.TestCase):

    def setUp(self):
        self.converter = Converter()

    def test_dict_to_str(self):
        input_data = {
            "h1": [{'p': 'p 1', 'header': 'header 1'}],
            "p": "Body 1"
        }
        result = self.converter.dict_to_str(input_data)
        self.assertEqual(result, '<h1><ul><li><p>p 1</p><header>header 1</header></li></ul></h1><p>Body 1</p>')

    def test_list_creator(self):
        input_data = [
            {"span": "span 1",
             "content": [
                 {
                     "p": "p 1",
                     "header": "header 1"
                 }
             ]

             },
            {
                "div": "div 1"
            }
        ]
        result = self.converter.html_list_creator(input_data)
        self.assertEqual(result,
                         '<ul><li><span>span 1</span><content><ul><li><p>p 1</p><header>header 1</header></li></ul></content></li><li><div>div 1</div></li></ul>')


if __name__ == "__main__":
    unittest.main()
