from argparse import ArgumentParser

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep


class AutoLoginService:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.arguments = self.parse_arguments()
        try:
            self.file = open(self.arguments.file, 'r')
        except FileNotFoundError:
            print('Такого файла нет')

    def parse_arguments(self):
        parser = ArgumentParser()
        parser.add_argument('--link', type=str, required=True)
        parser.add_argument('--file', type=str, required=True)
        return parser.parse_args()

    def run(self):

        self.driver.get(self.arguments.link)
        try:
            for line in self.file:
                login, password = line.split()
                self.driver.find_element(By.ID, 'user_login').send_keys(login)
                self.driver.find_element(By.ID, 'user_password').send_keys(password)
                self.driver.find_element(By.XPATH, '//*[@id="new_user"]/div[5]/input').click()
                sleep(1)
        except AttributeError:
            print('Файл или ссылка не загружены')