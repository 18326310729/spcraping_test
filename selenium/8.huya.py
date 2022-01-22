from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Huya(object):
    def __init__(self):
        self.url = 'https://www.huya.com/g/wzry'
        self.driver = webdriver.Chrome()

    def parse_data(self):
        # room_list = self.driver.find_elements_by_xpath('//*[@id="js-live-list"]/li')
        room_list = self.driver.find_element(By.XPATH, '//*[@id="js-live-list"]/li')
        # print(len(room_list))
        data_list = []
        for room in room_list:
            temp = {}
            # temp['title'] = room.find_element_by_xpath('./a[2]').text
            temp['title'] = room.find_element(By.XPATH, './a[2]').text
            temp['owner'] = room.find_element(By.XPATH, './span/span[1]/i').text
            temp['num'] = room.find_element(By.XPATH, './span/span[2]/i[2]').text    
            temp['png'] = room.find_element(By.XPATH, './a[1]/img').get_attribute('src')
            data_list.append(temp)
        return data_list

    def save(self, data_list):
        for data in data_list:
            print(data)

    def run(self):
        self.driver.get(self.url)
        while True:
            time.sleep(5)
            data_list = self.parse_data()
            self.save(data_list)

            try:
            # el_next = self.driver.find_element_by_xpath('//*[@class="laypage_next"]')
                el_next = self.driver.find_element(By.XPATH, '//*[contains(text(), "下一页")]')
                self.driver.execute_script('scrollTo(0, 100000)')
                el_next.click()
            except:
                break


if __name__ == '__main__':
    huya = Huya()
    huya.run()