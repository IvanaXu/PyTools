#
from selenium import webdriver

url = "https://www.baidu.com"

# http://npm.taobao.org/mirrors/chromedriver/
browser = webdriver.Chrome(executable_path="./061.Test_selenium_WebAuto_chromedriver")

browser.get(url)

print(browser.page_source)



