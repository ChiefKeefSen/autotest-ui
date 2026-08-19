from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login',
        wait_until='networkidle'
    )

    #ошибка неизвестный локатор
    # unknown = page.locator('#unknown')
    # expect(unknown).to_be_visible()
  #   Error: element(s) not found
  #   Call log:
  # - Expect "to_be_visible" with timeout 5000ms
  # - waiting for locator("#unknown")

    #неправильное взаимодействие с предметом на странице
    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill("aboba")
    #60 × waiting for element to be visible, enabled and editable
    # - element is not enabled

    #неправильный evaluate
    page.evaluate(
        """
        (text) => {
            const title = document.getElementById('authentication-ui-course-title-text')
            title.textContent = "12345text"
        }
        """
    )
    page.wait_for_timeout(1000)
    #TypeError: Cannot set properties of null (setting 'textContent')  #не прогрузилась страница
