import json
from json.decoder import JSONDecodeError


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
            html_str += f'<{key}>{value}</{key}>'

        return html_str

    def html_list_creator(self, data):
        """ Создадим список HTML """
        html_data = ''
        for json_dict in data:
            html_data += '<li>{}</li>'.format(self.dict_to_str(json_dict))

        return '<ul>{}</ul>'.format(html_data)


if __name__ == '__main__':
    Converter().get_file()
