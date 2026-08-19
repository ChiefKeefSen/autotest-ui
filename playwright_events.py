from playwright.sync_api import sync_playwright, Request, Response

def log_request(request: Request):
    print(f'Request: {request.url}')

def log_response(response: Response):
    print(f'Response: {response.url}') #тут и выше в функции
    #можно доп обработку, доп инфу выводить


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    page.on('request', log_request) #1 аргумент это что ловим, 2 - как обрабатываем
    #page.remove_listener('request', log_request) #можно также удалить обработчик (в консоли только респонсы будут)
    page.on('response', log_response) #причем функции передаешь без вызова

    page.wait_for_timeout(5000)