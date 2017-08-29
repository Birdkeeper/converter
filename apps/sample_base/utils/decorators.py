from django.http import JsonResponse

from sample_base.utils.exceptions import JsonValidatorException


def validate_input_data(list_classes_validators=None):
    """
    Декоратор проверяет входные данные, проходя в цикле по списку валидаторов.
    При неудачной валидации отправляет JsonResponse с ошибкой

    :param list_classes_validators: список валидаторов
    :type list_classes_validators: list
    """
    def check_data_decorator(view_func):
        def wrapper(request):
            request = request.body.decode('utf-8')
            for class_validator in list_classes_validators:
                try:
                    class_validator.validate(request)
                except JsonValidatorException as err:
                    return JsonResponse(
                        {'error': err.message},
                        json_dumps_params={'ensure_ascii': False}
                    )
            return view_func(request)
        return wrapper
    return check_data_decorator
