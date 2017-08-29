from django.conf import settings

from sample_base.utils.base_html_generator import BaseHtmlGenerator


class HtmlGenerator(BaseHtmlGenerator):

    MAX_LEVEL = 10

    @classmethod
    def parse_list_json(cls, json_input, level=0):
        """
        Если на входе был принят словарь, то вызывается метод parse_dict_json.
        Если на вход был принят список, то проходим по нему в цикле и
        вызываем рекурсию

        :param json_input: данные, которые будут обрабатываться парсером
        :type json_input: dict or list
        :param level: текущий обрабатываемый уровень вложенности
        :type level: int
        :return: сгенерированная html строка
        :rtype: str
        """
        result = ''
        if level > cls.MAX_LEVEL:
            return result

        if isinstance(json_input, list):
            content = ''.join(
                [cls.parse_list_json(child, level+1) for child in json_input]
            )
            return "<ul>{content}</ul>".format(content=content)

        if isinstance(json_input, dict):
            return "<li>{content}</li>".format(
                content=cls.parse_dict_json(json_input)
            )

        return result

    @staticmethod
    def convert_to_html(json_input):
        result = []
        for key, value in json_input.items():
            value = value or ""
            tag = settings.CONVERSION_TABLE.get(key, key)
            result.append(
                "<{tag}>{value}</{tag}>".format(
                    tag=tag,
                    value=value
                )
            )
        return result
