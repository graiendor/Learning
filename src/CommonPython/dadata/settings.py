import sqlite3


def settings():
    """Загружает базу данных с настройками или создает новую с дефолтной записью."""
    with sqlite3.connect('settings.db') as settings:
        settings.text_factory = str
        cur = settings.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS  settings (
        id INTEGER NOT NULL PRIMARY KEY,
        url TEXT NOT NULL DEFAULT "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address",
        token TEXT,
        lang TEXT NOT NULL DEFAULT "ru")
        ''')
        if not cur.execute('SELECT id FROM settings WHERE id = 1').fetchone():
            print('Введите, пожалуйста, токен авторизации с dadata.ru:')
            cur.execute(f'INSERT INTO settings VALUES (1, '
                        f'"https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address", '
                        f'"{input()}", '
                        f'"ru")')
        token = cur.execute('SELECT token FROM settings').fetchone()[0]
        url = cur.execute('SELECT url FROM settings').fetchone()[0]
        language = cur.execute('SELECT lang FROM settings').fetchone()[0]
        if not token:
            print('Введите, пожалуйста, токен авторизации с dadata.ru:')
            cur.execute(f'UPDATE settings SET token = "{input()}" WHERE id = 1')
        return url, token, language


def change_settings(position: int):
    """Изменяет соответствующе значение в базе данных согласно позиции:
    1. URL
    2. Token
    3. Язык"""
    with sqlite3.connect('settings.db') as settings:
        choice: list[str] = ['url', 'token', 'lang']
        settings.text_factory = str
        cur = settings.cursor()
        value = input()
        cur.execute(f'UPDATE settings SET {choice[position - 1]} = "{value}" WHERE id = 1')
    return value
