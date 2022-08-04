from settings import settings
import requests


class Configuration():
    """Класс, хранящий в себе необходимые данные для запросов"""
    def __init__(self, url: str, token: str, language: str):
        self.url = url
        self.token = token
        self.language = language


precision: list = ['точные координаты',
                   'ближайший дом',
                   'улица',
                   'населенный пункт',
                   'город',
                   'координаты не определены']


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


def select_case(configuration: Configuration) -> None:
    """Собственно меню"""
    stop = False
    print('Пожалуйста, выберите нужный вариант из списка:\n'
          '1. Узнать координаты адреса.\n'
          '2. Выйти из программы.')
    while not stop:
        choice = input()
        match choice:
            case "1":
                print('Введите, пожалуйста, адрес:')
                address = input()
                stop = find_address(address, configuration)
            case "2":
                stop = True
            case _:
                 print('Пожалуйста, выберите вариант из списка\n'
                       '1. Узнать координаты адреса.\n'
                       '2. Выйти из программы.')


def errorhandler(status_code: int):
    success: bool = False
    match status_code:
        case 200:
            success = True
        case 400:
            print('Плохой запрос. Возможно, url или язык указаны неверно.')
        case 401:
            print('Авторизация прошла неуспешно, проверьте, пожалуйста, токен авторизации.')
        case _:
            print('Что-то пошло не так')
    return success


def find_address(address: str, configuration: Configuration) -> bool:
    """Собственно работа с API dadata"""
    headers = {"Content-Type": "application/json", "Accept": "application/json", "Authorization": f'Token {configuration.token}'}
    response = requests.post(url="http://vk.com", headers=headers, json={"query": address, "language": configuration.language})
    stop = False
    if errorhandler(response.status_code):
        try:
            suggestions = response.json()['suggestions']
            for counter, suggestion in enumerate(suggestions):
                print(f"{counter + 1}: {suggestion['value']}")
            if len(suggestions) < 1:
                print('Такого адреса не найдено.')
            else:
                choice = input_num(len(suggestions))
                print(suggestions[choice - 1]['value'])
                info = requests.post(url=configuration.url, headers=headers, json={"query": suggestions[choice]['value'], "language": configuration.language, "count": 1}).json()['suggestions']
                print(f"Координаты длины: {info[0]['data']['geo_lat']}")
                print(f"Координаты широты: {info[0]['data']['geo_lon']}")
                print(f"Точность определенных координат: {precision[int(info[0]['data']['qc_geo'])]}")
        except:
            print('Ответ сервера не соответствует ожиданиям. Возможно, url не тот.')
            stop = True
    else:
        stop = True
    return stop


def main() -> None:
    url, token, language = settings()
    if not token:
        print('Пожалуйста, поместите валидный токен в файл token.txt и повторите запуск')
    else:
        select_case(Configuration(url, token, language))


if __name__ == '__main__':
    main()
