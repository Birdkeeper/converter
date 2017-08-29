class JsonValidatorException(Exception):
    """
    Пользовательский класс исключений
    """

    def __init__(self, text):
        self.message = text
        super().__init__()

    def __str__(self):
        return self.message
