from django.test import TestCase


class ConverterHtmlTestCase(TestCase):

    URL = '/api/sample_3'

    def test_request_to_html_views(self):
        """
        Проверяет, что возвращается код статуса 200
        """
        response = self.client.post(
            self.URL,
            '[{"title": "Title #1", "body": "Hello, World 1!" }]',
            'application/json'
        )
        self.assertEquals(response.status_code, 200)

    def test_html_generator(self):
        """
        Сверяется результат работы функции с эталонным
        """
        response = self.client.post(
            self.URL,
            '[{"title": "Body1", "body": "Body2"}]',
            'application/json'
        )
        self.assertEquals(
            response.content, b'<ul><li><h1>Body1</h1><p>Body2</p></li></ul>'
        )
