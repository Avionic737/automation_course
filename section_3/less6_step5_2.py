import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestMainPage:

    msg = []
    '''
    link = [
            "https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
            "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
            "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
            "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"
            ]
    '''

    @pytest.mark.parametrize('links', [
            "https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
            "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
            "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
            "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"
            ])
    def test_login(self, browser, links):
        browser.implicitly_wait(30)
        browser.get(links)
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

        time.sleep(7)

        # button3 = WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
        #                                                                       "button.again-btn")))
        # button3.click()

        # button4 = WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
        #                                                                      "button[data-ember-action-109='109']")))
        # button4.click()

        answer = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area")
        answer.send_keys(math.log(int(time.time()+59.8)))
        time.sleep(3)

        """
        if button3:
            # Если кнопка button3 найдена, нажмите на нее
            button3[0].click()
            time.sleep(3)
            alert = browser.switch_to.alert
            alert.accept()
            browser.switch_to.default_content()
        else:
            # Если кнопка button3 не найдена, перейдите к пункту answer
            answer = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area")
            answer.send_keys(str(math.log(int(time.time()))))
        """

        # button5 = WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR,
        #                                                                        "button.submit-submission")))

        button5 = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
        button5.click()

        time.sleep(3)
        element = browser.find_element(By.CSS_SELECTOR, "div.smart-hints p.smart-hints__hint")
        # Получаем текст из элемента
        text_on_page = element.text
        self.msg.append(text_on_page)

        # Ожидаемый текст
        expected_text = "Correct!"

        # Проверяем текст на соответствие ожидаемому
        assert text_on_page == expected_text, f"Текст на странице: '{text_on_page}', ожидался текст: '{expected_text}'"


if __name__ == "__main__":
    pytest.main()
    print("Contents of the msg list:", TestMainPage.msg)

# pytest -v -s less6_step5_2.py
