from playwright import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch()
    page = browser.newPage()
    page.goto('https://www.example.com/')
    dimensions = page.evaluate('''() => {
      return {
        width: document.documentElement.clientWidth,
        height: document.documentElement.clientHeight,
        deviceScaleFactor: window.devicePixelRatio
      }
    }''')
    print(dimensions)
    browser.close()
