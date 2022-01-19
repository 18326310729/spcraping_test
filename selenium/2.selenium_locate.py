from lib2to3.pgen2 import driver
from selenium import webdriver

url = 'https://baidu.com'
driver = webdriver.Chrome()
driver.get(url)

# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
# driver.find_element_by_css_selector('#kw').send_keys('python')
# driver.find_element_by_class_name('s_ipt').send_keys('python')
# driver.find_element_by_name('wd').send_keys('python')
# driver.find_element_by_name('wd').send_keys('python')

# driver.find_element_by_id('su').click()

# driver.find_element_by_link_text('hao123').click()
driver.find_element_by_partial_link_text('hao').click()
# driver.quit()