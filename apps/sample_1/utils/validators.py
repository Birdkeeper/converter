from django.conf import settings

from sample_base.utils.exceptions import JsonValidatorException
from sample_base.utils.base_validators import BaseValidator


class KeyValidator(BaseValidator):
    """
    Класс для проверки ключей в JSON
    """
    @classmethod
    def validate(cls, input_json):
        for k, v in input_json.items():
            if not (k in settings.CONVERSION_TABLE):
                raise JsonValidatorException(
                    "Ключ '{key}' не найден "
                    "в таблице преобразований".format(key=k)
                )
