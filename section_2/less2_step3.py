from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def calc(x, y):
    return str(int(x) + int(y))


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = x_element.text  # Извлекаем текст из элемента
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = y_element.text  # Извлекаем текст из элемента
    z = calc(x, y)

    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(z)  # ищем элемент

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
