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

        with open(self.output_file, 'w+') as html_file:
            html_data = ''.join(map(self.dict_to_str, json_data))
            html_file.write(html_data)

    def dict_to_str(self, json_dict) -> str:
        """ Преобразуем json_dict в строку с HTML тегами"""

        html_str = ''
        try:
            title = json_dict['title']
            html_str += f'<h1>{title}</h1>'
        except KeyError:
            print('Key "title" was not found')

        try:
            paragraph = json_dict['body']
            html_str += f'<p>{paragraph}</p>'
        except KeyError:
            print('Key "body" was not found')

        return html_str


if __name__ == '__main__':
    Converter().get_file()
