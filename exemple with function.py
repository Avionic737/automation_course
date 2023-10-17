def send_answer(answer, link):
    #в функцию передаем ответ и ссылку текущего урока

    browser = webdriver.Chrome()

    email = '****@***.**' #ваша почта на степике
    password = '******' #ваш пароль

    browser.get(link)
    time.sleep(5)

    current_url = str(browser.current_url)
    if 'promo' in current_url:
        browser.get(current_url + '?auth=login')
        time.sleep(3)
        browser.find_element_by_css_selector('[name = "login"]').send_keys(email)
        browser.find_element_by_css_selector('[name = "password"]').send_keys(password)
        time.sleep(3)
        browser.find_element_by_css_selector(".sign-form__btn").click()
        time.sleep(1)

    browser.get(link)
    time.sleep(5)
    right = browser.find_element_by_css_selector('div[data-type="string-quiz"]').get_attribute('data-state')
    if right == 'no_submission':
        browser.find_element_by_css_selector('textarea[placeholder="Напишите ваш ответ здесь..."]').clear()
        time.sleep(1)
        browser.find_element_by_css_selector('textarea[placeholder="Напишите ваш ответ здесь..."]').send_keys(answer)
    else:
        browser.find_element_by_css_selector('button[class="again-btn white"]').click()
        time.sleep(1)
        browser.find_element_by_css_selector('footer[class="modal-popup__footer ember-view"] :first-child').click()
        time.sleep(1)
        browser.find_element_by_css_selector('textarea[placeholder="Напишите ваш ответ здесь..."]').clear()
        time.sleep(1)
        browser.find_element_by_css_selector('textarea[placeholder="Напишите ваш ответ здесь..."]').send_keys(answer)
    time.sleep(1)
    browser.find_element_by_css_selector('button[class ="submit-submission"]').click()


# основная программа урока
try:
    #...
    answer = browser.switch_to.alert.text.split()[-1]

finally:
    #если что-то пошло не так можно отменить отправку
    send = input(f'Отослать ответ: {answer}? Y/N')
    if send in ['Y', 'y', 'Н', 'н']: send_answer(answer, 'https://stepik.org/lesson/184253/step/6?unit=158843')
    time.sleep(5)
    browser.quit()