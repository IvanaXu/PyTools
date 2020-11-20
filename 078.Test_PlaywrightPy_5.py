from playwright import sync_playwright

with sync_playwright() as p:
    iphone_11 = p.devices['iPhone 11 Pro']
    browser = p.webkit.launch(headless=False)
    context = browser.newContext(
        **iphone_11,
        locale='en-US',
        geolocation={
            'longitude': 12.492507,
            'latitude': 41.889938
        },
        permissions=['geolocation'])
    page = context.newPage()
    # page.goto('https://maps.google.com')
    page.goto('https://map.baidu.com/')
    page.click('text="Your location"')
    page.screenshot(path='colosseum-iphone.png')
    browser.close()
