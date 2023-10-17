"""
Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла
Просмотрите отчёт о запуске и найдите последнюю строчку
Отправьте эту строчку в качестве ответа на это задание
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestForms(unittest.TestCase):
    def test1(self):

        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(
                By.CSS_SELECTOR,
                "div.first_block div.form-group.first_class input.form-control.first",
            )
            input1.send_keys("1")
            input2 = browser.find_element(
                By.CSS_SELECTOR,
                "div.first_block div.form-group.second_class input.form-control.second",
            )
            input2.send_keys("2")
            input2 = browser.find_element(
                By.CSS_SELECTOR,
                "div.first_block div.form-group.third_class input.form-control.third",
            )
            input2.send_keys("3")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Text not equal")
            # assert "Congratulations! You have successfully registered!" == welcome_text

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test2(self):

        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(
                By.CSS_SELECTOR,
                "div.first_block div.form-group.first_class input.form-control.first",
            )
            input1.send_keys("1")
            input2 = browser.find_element(
                By.CSS_SELECTOR,
                "div.first_block div.form-group.second_class input.form-control.second",
            )
            input2.send_keys("2")
            input2 = browser.find_element(
                By.CSS_SELECTOR,
                "div.first_block div.form-group.third_class input.form-control.third",
            )
            input2.send_keys("3")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Text not equal")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()

