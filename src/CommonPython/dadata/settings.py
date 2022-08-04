import sqlite3


def read_token() -> str:
    """Читает токен из файла"""
    with open('token.txt') as file:
        return file.readline()


def settings():
    """Загружает базу данных с настройками или создает новую с дефолтной записью."""
    with sqlite3.connect('settings.db') as settings:
        settings.text_factory = str
        cur = settings.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS  settings (
        id INTEGER NOT NULL PRIMARY KEY,
        url TEXT NOT NULL DEFAULT "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address",
        token TEXT,
        language TEXT NOT NULL DEFAULT "ru")
        ''')
        if not cur.execute('SELECT id FROM settings WHERE id = 1').fetchone():
            cur.execute(f'INSERT INTO settings VALUES (1, '
                        f'"https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address", '
                        f'"{read_token()}", '
                        f'"ru")')
        token = cur.execute('SELECT token FROM settings').fetchone()[0]
        url = cur.execute('SELECT url FROM settings').fetchone()[0]
        language = cur.execute('SELECT language FROM settings').fetchone()[0]
        if not token:
            cur.execute(f'UPDATE settings SET token = "{read_token()}" WHERE id = 1')
        return url, token, language
