import time
from selenium.webdriver.support import expected_conditions as ec
import pytest
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

"""
link = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"]
"""
link = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1"]


def test_guest_should_see_login_link(browser, page_link):
    browser.implicitly_wait(30)
    browser.get(page_link)
    button = browser.find_element(By.CSS_SELECTOR,
                                  ".ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button")
    button.click()
    browser.implicitly_wait(30)
    login = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
    login.send_keys("")
    passw = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    passw.send_keys("")

    button2 = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader")
    button2.click()

    time.sleep(10)

    answer = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area")
    answer.send_keys(math.log(int(time.time())))

    button3 = WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                                          "button.submit-submission")))
    button3.click()

    time.sleep(3)
    element = browser.find_element(By.CSS_SELECTOR, "div.smart-hints p.smart-hints__hint")
    # Получаем текст из элемента
    text_on_page = element.text

    # Ожидаемый текст
    expected_text = "Correct!"

    # Проверяем текст на соответствие ожидаемому
    assert text_on_page == expected_text, f"Текст на странице: '{text_on_page}', ожидался текст: '{expected_text}'"


@pytest.mark.parametrize('page_link', link)
def test_with_link_param(browser, page_link):
    test_guest_should_see_login_link(browser, page_link)


if __name__ == "__main__":

    pytest.main()

# pytest -v -s less6_step5.py
