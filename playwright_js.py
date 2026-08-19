from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login',
        wait_until='networkidle' #подождет пока выполнятся все запросы (откроется страница и выполнится весь ее код)
    )


    text = "12345"
    page.evaluate( #так работает evaluate он этот код в js выполняет
        """
        (text) => {
            const title = document.getElementById('authentication-ui-course-title-text')
            title.textContent = text
        }
        """,
        text #а аргументы после выражения ебать
    ) #ВСЕГДА сначала пытайся протестить с помощью playwright и только потом если ничего не получилось то с помощью JS
    # и сам JS код выполняется только после полной прогрузки страницы
    page.wait_for_timeout(5000)