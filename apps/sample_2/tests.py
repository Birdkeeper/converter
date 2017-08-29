from django.test import TestCase


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

    def test_html_generator(self):
        """
        Проверяет результат работы функции с эталонным
        """
        response = self.client.post(
            '/api/sample_1',
            '[{"title": "Body1", "body": "Body2"}]',
            'application/json'
        )
        self.assertEquals(response.content, b'<h1>Body1</h1><p>Body2</p>')
