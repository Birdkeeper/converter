import json
from abc import ABCMeta, abstractclassmethod
from json.decoder import JSONDecodeError

from django.conf import settings

from sample_base.utils.exceptions import JsonValidatorException


class BaseValidator:
    """
    Абстрактный класс валидации
    """
    __metaclass__ = ABCMeta

    @abstractclassmethod
    def validate(self, obj):

        raise NotImplementedError(
            "Определите метод validate в"
            " классе {class_name}".format(class_name=self.__name__)
        )


class JsonValidator(BaseValidator):
    """
    Класс для проверки входных данных на правильный JSON
    """

    @classmethod
    def validate(cls, json_input):
        try:
            json.loads(json_input)
        except (TypeError, JSONDecodeError):
            raise JsonValidatorException(
                "При проверке входные данные оказались не в формате JSON"
            )


class SizeValidator(BaseValidator):
    """
    Класс для проверки размера входных данных
    """

    @classmethod
    def validate(cls, input_json):
        if settings.JSON_LEN:
            if len(input_json) > settings.JSON_LEN:
                raise JsonValidatorException(
                    "Слишком большой размер входных данных"
                )
