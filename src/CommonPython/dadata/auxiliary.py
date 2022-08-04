class Configuration():
    """Класс, хранящий в себе необходимые данные для запросов"""
    def __init__(self, url: str, token: str, language: str):
        self.url = url
        self.token = token
        self.language = language


def input_num(length: int) -> int:
    """Проверяет ввод на вхождение в диапазон допустимых значений"""
    integer: bool = False
    value = 0
    while not integer:
        value = input()
        try:
            value = int(value)
            assert 1 <= value < length
            integer = True
        except AssertionError:
            print('Нужно выбрать число в пределах вышеприведенного списка.')
        except ValueError:
            print('Нужно выбрать именно число.')
    return value