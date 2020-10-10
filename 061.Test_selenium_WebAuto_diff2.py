#
from selenium import webdriver

url = "https://www.baidu.com"

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"

# 伪装user_agent 并进一步反爬虫
opt = webdriver.ChromeOptions()
opt.add_argument('--user-agent=%s' % user_agent)
opt.add_experimental_option('excludeSwitches', ['enable-automation'])
opt.add_experimental_option('useAutomationExtension', False)

# http://npm.taobao.org/mirrors/chromedriver/
browser = webdriver.Chrome(
    executable_path="./061.Test_selenium_WebAuto_chromedriver", options=opt)
browser.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument", {
        "source":
        """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
    })

browser.get(url)

print(browser.page_source)
