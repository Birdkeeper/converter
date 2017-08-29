from collections import OrderedDict

from django.test import TestCase

from sample_1.utils.html_generator import HtmlGenerator
from sample_1.utils.validators import KeyValidator
from sample_base.utils.exceptions import JsonValidatorException


class ConverterHtmlTestCase(TestCase):

    def test_request_to_html_views(self):
        """
        Проверяет, что возвращается код статуса 200
        """
        response = self.client.post(
            '/api/sample_1',
            '[{"title": "Title #1", "body": "Hello, World 1!" }]',
            'application/json'
        )
        self.assertEquals(response.status_code, 200)

    def test_key_validator(self):
        """
        Проверяет работоспосоность валидатора при неверных входных данных
        """
        with self.assertRaises(JsonValidatorException):
            KeyValidator.validate([{'titele': 'Body1', 'body': 'Body2'}])
