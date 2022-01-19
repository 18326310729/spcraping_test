from selenium import webdriver

# 创建配置对象
opt = webdriver.ChromeOptions()

# 添加配置参数
# 设置浏览器为无界面模式
# opt.add_argument('--headless')  # 开启无界面模式
# opt.add_argument('--disable-gpu')  # 禁用gpu

# 更换ip代理，必须重新启动浏览器
# opt.add_argument('--proxy-server=http://122.226.57.70:8888')

# 更换user-agent
opt.add_argument('--user-agent=Mozilla/5.0 Python')

driver = webdriver.Chrome(chrome_options=opt)
driver.get('https://www.baidu.com/')
# print(driver.title)