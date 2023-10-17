"""
1 Открыть страницу http://suninjuly.github.io/file_input.html
2 Заполнить текстовые поля: имя, фамилия, email
3 Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
4 Нажать кнопку "Submit"
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@test.com")

    with open("file.txt", "w") as file:
        content = file.write("automationbypython")  # create test.txt file

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)



    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

