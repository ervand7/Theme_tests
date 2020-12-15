import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

my_login = ''
my_password = ''


class YandexPassportTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()
        self.driver.minimize_window()
        self.driver.get('https://passport.yandex.ru/auth')

    def test_search(self):
        time.sleep(1)
        elem = self.driver.find_element_by_name('login')
        elem.send_keys(my_login)

        time.sleep(1)
        self.driver.find_element(By.XPATH, '//button[span="Войти"]').click()

        time.sleep(1)
        elem = self.driver.find_element_by_name('passwd')
        elem.send_keys(my_password)

        time.sleep(1)
        self.driver.find_element(By.XPATH, '//button[span="Войти"]').click()

        time.sleep(6)
        self.assertIn("Яндекс.Паспорт", self.driver.title)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()