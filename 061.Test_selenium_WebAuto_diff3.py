#
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

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
wait = WebDriverWait(browser, 30)
browser.get(url)
# F11 Copy Xpath
browser.find_element_by_xpath("""//*[@id="kw"]""").send_keys("10086")

# F11 Copy JSpath
browser.execute_script("""document.querySelector("#su").click()""")

print(browser.page_source)

# 036.PyCrawler_Spiget
