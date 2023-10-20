import time

from selenium.webdriver.common.by import By

link = "https://stepik.org/lesson/236895/step/1"


def test_guest_should_see_login_link(browser):
    browser.implicitly_wait(30)
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR,
                                  ".ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button")
    button.click()
    browser.implicitly_wait(30)
    login = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
    login.send_keys("yury.halyha@gmail.com")
    passw = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    passw.send_keys("uyJv152987.")

    button2 = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader")
    button2.click()
    time.sleep(20)
