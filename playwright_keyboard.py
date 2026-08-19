from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()

    #page.keyboard.insert_text("user_email.com") # первый вариант печати всего текста

    for char in "user.name@gmail.com":
        email_input.type(char, delay=150) #вот второй вариант где type напечатать 1 символ


    page.keyboard.press('ControlOrMeta+A') #есть еще press, но он скорее для комбинации клавиш
    page.wait_for_timeout(5000)



#есть сайт playwright с докой для питона