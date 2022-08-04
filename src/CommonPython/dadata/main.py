from settings import settings, change_settings
from auxiliary import Configuration, input_num
import requests

precision: list = ['точные координаты',
                   'ближайший дом',
                   'улица',
                   'населенный пункт',
                   'город',
                   'координаты не определены']


def change_settings_menu(configuration: Configuration):
    """Меню для выбора, какую позицию изменить в настройках"""
    stop: bool = False
    while not stop:
        print('Выберите, пожалуйста, что вы хотите изменить:\n'
              '1. URL запроса.\n'
              '2. Токен авторизации.\n'
              '3. Язык (только en или ru)\n'
              '4. Ничего (вернуться к выполнению программы)')
        choice = input()
        match choice:
            case "1":
                configuration.url = change_settings(1)
            case "2":
                configuration.token = change_settings(2)
            case "3":
                print('yes')
                configuration.language = change_settings(3)
            case "4":
                stop = True
            case _:
                print('Пожалуйста, выберите вариант из списка:\n'
                      '1. URL запроса.\n'
                      '2. Токен авторизации.\n'
                      '3. Язык (только en или ru)\n'
                      '4. Ничего (вернуться к выполнению программы)')


def select_case(configuration: Configuration) -> None:
    """Собственно меню"""
    stop = False
    while not stop:
        print('Пожалуйста, выберите нужный вариант из списка:\n'
              '1. Узнать координаты адреса.\n'
              '2. Изменить настройки.\n'
              '3. Выйти из программы.')
        choice = input()
        match choice:
            case "1":
                print('Введите, пожалуйста, адрес:')
                address = input()
                stop = find_address(address, configuration)
            case "2":
                change_settings_menu(configuration)
            case "3":
                stop = True
            case _:
                 print('Пожалуйста, выберите вариант из списка\n'
                       '1. Узнать координаты адреса.\n'
                       '2. Выйти из программы.')


def errorhandler(status_code: int):
    """Обрабатывает типовые ситуации, когда возвращается код ошибки"""
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
    response = requests.post(url=configuration.url, headers=headers, json={"query": address, "language": configuration.language})
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
