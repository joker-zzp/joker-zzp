#! /usr/bin/python3

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# driver = webdriver.Chrome()
# driver.close()
driver = webdriver.Firefox()

driver.get("http://www.baidu.com")

assert "百度一下，你就知道" in driver.title
element = driver.find_element_by_id("kw")

element.send_keys('中华')
time.sleep(1)
submit = driver.find_element_by_id("su")
submit.click()
time.sleep(5)


suub = driver.find_element_by_xpath(
    "//a[contains(text(), '百度百科')]").click()
time.sleep(5)
print(driver.title)

# 关闭浏览器
driver.quit()

print("测试通过")
