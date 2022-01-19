from lib2to3.pgen2 import driver
from selenium import webdriver

url = 'https://qzone.qq.com'
driver = webdriver.Chrome()
driver.get(url)

# 方式一
# driver.switch_to.frame('login_frame')
# driver.find_element_by_id('switcher_plogin').click()
# driver.find_element_by_id('u').send_keys('1941142883')
# driver.find_element_by_id('p').send_keys('Ybx1997525')
# driver.find_element_by_id('login_button').click()

# 方式二
el_frame = driver.find_element_by_xpath('//*[@id="login_frame"]')
driver.switch_to.frame(el_frame)
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys('1941142883')
driver.find_element_by_id('p').send_keys('Ybx1997525')
driver.find_element_by_id('login_button').click()