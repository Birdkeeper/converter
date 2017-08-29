import json
from collections import OrderedDict

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from sample_3.utils.html_generator import HtmlGenerator
from sample_base.utils.base_validators import JsonValidator, SizeValidator
from sample_base.utils.decorators import validate_input_data


@csrf_exempt
@validate_input_data(list_classes_validators=[JsonValidator, SizeValidator])
def request_to_html(request):
    """Конвертирует JSON в HTML

    получаем тело запроса, который должен содержать JSON строку, проверяем
    на наличие ошибок. Конвертируем строку в JSON. Конвертируем
    в HTML с помощью класса HtmlGenerator

    :param request: объект WSGI реквеста
    :return: JsonResponse с ошибкой валидации, либо HttpResponse со
    сгенерированной HTML строкой
    :rtype: JsonResponse or HttpResponse
    """

    json_input = json.loads(request, object_pairs_hook=OrderedDict)
    try:
        response = HtmlGenerator.parse_json(json_input)
    except NotImplementedError as err:
        return JsonResponse(
            {'error': err.args[0]}, json_dumps_params={'ensure_ascii': False}
        )

    return HttpResponse(response)
