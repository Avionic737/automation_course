from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button1 = browser.find_element(By.ID, "book")
    button1.click()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    # x = x_element.text
    y = calc(x)

    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    # Ввести текст в поле ввода
    input_field.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()
