from playwright import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.newPage()

    def log_and_continue_request(route, request):
        print(request.url)
        route.continue_()

    # Log and continue all network requests
    page.route('**',
               lambda route, request: log_and_continue_request(route, request))

    page.goto('http://todomvc.com')
    browser.close()
