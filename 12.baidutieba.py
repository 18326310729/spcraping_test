from json.tool import main
from pkgutil import get_data
from urllib import response
import requests
from lxml import etree

class Tieba(object):
    def __init__(self, name):
        self.url = 'https://tieba.baidu.com/f?kw={}'.format(name)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
        }

    def get_data(self, url):
        response = requests.get(self.url, headers=self.headers)
        return response.content

    def parse_data(self, data):
        # 创建element对象
        data = data.decode().replace("<!--", "").replace("-->", "")
        html = etree.HTML(data)
        ele_list = html.xpath('//*[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a')
        print(len(ele_list))

        data_list = []
        for el in ele_list:
            temp = {}
            temp['title'] = el.xpath('./text()')[0]
            temp['link'] = 'https://tieba.baidu.com/' + el.xpath('./@href')[0]
            data_list.append(temp)

        # 获取下一页
        try:
            next_url = 'https:' + html.xpath('//a[contains(text(), "下一页>")]/@href')[0]
            # print(next_url)
        except:
            next_url = None

        return data_list, next_url

    def save_data(self, data_list):
        for data in data_list:
            print(data)

    def run(self):
        next_url = self.url
        while True:
            data = self.get_data(next_url)
            # 从响应中提取数据
            data_list, next_url = self.parse_data(data)
            self.save_data(data_list)
            # print(next_url)
            if next_url is None:
                break


if __name__ == '__main__':
    tieba = Tieba('传智播客')
    tieba.run()