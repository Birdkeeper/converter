from abc import ABCMeta, abstractclassmethod


class BaseHtmlGenerator:

    __metaclass__ = ABCMeta

    @classmethod
    def parse_json(cls, json_input):
        """Обрабатывает введенный JSON в зависимости от его типа

        Если на входе был принят словарь, то вызывается метод parse_dict_json.
        Если на вход был принят список,то вызывается метод parse_list_json,
        который также должен быть переопределен

        :param json_input: данные, которые будут обрабатываться парсером
        :type json_input: dict or list
        :return: сгенерированная html строка
        :rtype: str
        """
        result = ""

        if isinstance(json_input, list):
            return cls.parse_list_json(json_input)

        if isinstance(json_input, dict):
            return cls.parse_dict_json(json_input)
        return result

    @abstractclassmethod
    def parse_list_json(self, json_input):
        raise NotImplementedError(
            "Определите метод parse_list_json в"
            " классе {class_name}".format(class_name=self.__name__)
        )

    @classmethod
    def parse_dict_json(cls, json_input):
        """
        Вызывает метод convert_to_html, который конвертирует словарь в  html.

        :param json_input: Данные, которые необходисо обработать
        :type json_input: dict
        :return: сгенерированная html строка
        :rtype: str
        """
        return ''.join(cls.convert_to_html(json_input))

    @abstractclassmethod
    def convert_to_html(self, json_input):
        raise NotImplementedError(
            "Определите метод convert_to_html в"
            " классе {class_name}".format(class_name=self.__name__)
        )
