import json
from html import escape
from json.decoder import JSONDecodeError
import re


class Converter:

    def __init__(self, source='source.json', output_file='index.html'):
        self.source = source
        self.output_file = output_file

    def get_file(self) -> None:
        """Получаем данные из json файла"""

        try:
            with open(self.source) as json_file:
                try:
                    json_data = json.load(json_file)
                    self.converter(json_data)

                except JSONDecodeError:
                    print('File source.json contains invalid data, JSON expected')

        except FileNotFoundError:
            print('File source.json not found in current directory')

    def converter(self, json_data) -> None:
        """ Записываем новые данные в HTML"""
        with open('index.html', 'w+') as html_file:

            if isinstance(json_data, list):
                html_data = self.html_list_creator(json_data)
            else:
                html_data = ''.join(self.dict_to_str(json_data))

            html_file.write(html_data)

    def dict_to_str(self, json_dict) -> str:
        """ Преобразуем json_dict в строку с HTML тегами"""
        html_str = ''

        for key, value in json_dict.items():

            open_tag, close_tag = self.parse_css_selectors(key)

            if isinstance(value, list):
                value = self.html_list_creator(value)
                html_str += f'<{open_tag}>{value}</{close_tag}>'
            else:
                value = escape(value)
                html_str += f'<{open_tag}>{value}</{close_tag}>'

        return html_str

    def html_list_creator(self, data) -> str:
        """ Создадим список HTML """
        html_data = ''
        for json_dict in data:
            html_data += '<li>{}</li>'.format(self.dict_to_str(json_dict))
        return '<ul>{}</ul>'.format(html_data)

    def parse_css_selectors(self, key) -> tuple:
        """ Парсим селекторы и возвращаем кортеж из открытого и закрытого HTML тэга """
        parse_tag = re.findall(r'^[^#\.]+', key)
        parse_id = re.findall(r'#([a-zA-Z0-9]+)', key)
        parse_class = re.findall(r'\.([a-zA-Z0-9]+)', key)

        if parse_tag:
            css_tag = ''.join(parse_tag)
        else:
            print(f'Tag name is missing in "{key}"')
            css_tag = ''

        if parse_class:
            css_class = ' class="{}"'.format(' '.join(parse_class))
        else:
            css_class = ''

        if parse_id:
            if len(parse_id) > 1:
                print(f'The number of id in "{key}" is greater than 1, I will use the first one for layout')
                css_id = ' id="{}"'.format(parse_id[0])
            else:
                css_id = ' id="{}"'.format(''.join(parse_id))
        else:
            css_id = ''

        opening_tag = css_tag + css_id + css_class

        return opening_tag, css_tag


if __name__ == '__main__':
    Converter().get_file()
