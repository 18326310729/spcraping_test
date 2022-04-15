import requests
from fake_useragent import UserAgent   # 导入请求头模块
from multiprocessing import Pool       # 导入进程池
import re
from bs4 import BeautifulSoup
import time
import pandas as pd                    # 导入pandas模块

class Spider():
    def __init__(self):
        self.info_urls = []    # 所有电影详情页的请求地址
        # 创建DataFrame临时表格
        self.df = pd.DataFrame(columns=('name', 'date', 'imdb', 'douban', 'lengh'))

    # 获取首页信息
    def get_home(self, home_url):
        headers ={'UserAgent': 'UserAgent().random'}    # 创建随机请求头
        home_response = requests.get(home_url, headers=headers)
        if home_response.status_code == 200:
            home_response.encoding = 'gb2312'
            html = home_response.text
            # 获取所有电影详情页地址
            detail_url = re.findall('<a href="(.*?)" class="ulink">', html)
            global info_urls
            self.info_urls.extend(detail_url)

    def get_info(self, url):
        print()
        headers ={'UserAgent': 'UserAgent().random'}    # 创建随机请求头
        info_response = requests.get(url, headers=headers)
        if info_response.status_code == 200:
            info_response.encoding = 'gb2312'
            # 创建Beautifulsoup对象，获取页面正文
            html = BeautifulSoup(info_response.text, 'html.parser')
            # try:
            #     # 获取迅雷下载地址
            #     download_url = re.findall()

            # 获取电影名称
            name = html.select('div[class="title_all"]')[0].text
            # print(name)
            # 将电影的详细信息进行处理，先去除所有html中的空格（\u3000），然后用◎将数据进行分割
            info_all = (html.select('div[id="Zoom"]')[0]).span.text.replace(' ', '').split('◎')
            date = info_all[8]      # 获取上映时间
            # print(date)
            imdb = info_all[9]      # 获取IMDb评分
            # print(imdb)
            douban = info_all[10]   # 获取豆瓣评分
            # print(douban)
            length = info_all[11]      # 获取片长
            # print(length)
            # # 将数据信息添加至DataFrame临时表格中
            self.df.loc[len(self.df)+1] = {'name': name, 'date': date, 'imdb': imdb,
                                 'douban': douban, 'length': length}


if __name__ == '__main__':
    # 主页请求地址
    home_url = ['https://www.ygdy8.com/html/gndy/dyzz/list_23_{}.html'.format(str(i)) for i in range(1,2)]
    # 创建自定义爬虫类对象
    s = Spider()
    # 方式一：串行爬取  记录时间
    start_time = time.time()
    for i in home_url:
        s.get_home(i)
    end_time = time.time()
    print('串行爬取耗时：', end_time-start_time)

    # 方式二：进程池创建4个进程
    start_time = time.time()
    pool = Pool(processes=2)
    pool.map(s.get_home, home_url)
    end_time = time.time()
    print('进程爬取耗时1：', end_time-start_time)

    # 爬取电影信息详情
    # 拼接详情页urls
    # print(s.info_urls)
    info_urls = ['https://www.ygdy8.com' + i for i in s.info_urls]
    info_start_time = time.time()          # 记录爬取电影详情信息的起始时间
    for i in info_urls:  # 循环遍历电影详情页请求地址
        s.get_info(i)  # 发送网络请求，获取每个电影详情信息
    info_end_time = time.time()  # 记录串行结束时间
    print('串行爬取电影详情信息耗时：', info_end_time - info_start_time)
    # 记录爬取电影详情信息的起始时间
    info_start_time = time.time()
    pool = Pool(processes=4)
    pool.map(s.get_info, info_urls)
    # 记录结束时间
    info_end_time = time.time()
    print('爬取电影详情信息耗时1：', info_end_time - info_start_time)
    # 将爬取电影的详细信息保存至excel文件中
    s.df.to_excel('movie_info.xlsx')

