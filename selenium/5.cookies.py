from lib2to3.pgen2 import driver
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
# print(driver.get_cookies())

cookies = {cookie['name']: cookie['value'] for cookie in driver.get_cookies()}
print(cookies)