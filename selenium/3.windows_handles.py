from lib2to3.pgen2 import driver
from selenium import webdriver

url = 'https://nj.58.com/'
driver = webdriver.Chrome()
driver.get(url)

print(driver.current_url)
print(driver.window_handles)

el = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/span[1]/a')
el.click()

# print(driver.current_url)
# print(driver.window_handles)

# driver.switch_to.window(driver.window_handles[-1])

# el_list = driver.find_elements_by_xpath('/html/body/div[6]/div[2]/ul/li/div[2]/h2/a')
# print(len(el_list))