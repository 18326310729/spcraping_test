from lib2to3.pgen2 import driver
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://nj.lianjia.com/')

# 滚动条的拖动
js = 'scrollTo(0, 2000)'
driver.execute_script(js)
el_button = driver.find_element_by_xpath('/html/body/div[11]/div/div[1]/div[1]/ul/li[1]/a')
el_button.click()