import requests
import re


def login():
    session = requests.session()
    session.headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    }

    # url1获取token
    url1 = 'https://github.com/login'
    res1 = session.get(url1).content.decode()
    # 正则提取
    # name="authenticity_token"alue="VyoO53yVSQmU8OjhC9t2HqNlPnUREIgu9cfCqTeHih5i4gz-I7_vzXhoRYc9S4BJ4eRH9-Ved8XUIwlC-qnQug" 
    token = re.findall('name="authenticity_token" value="(.*?)"', res1)

    # url2登录
    url2 = 'https://github.com/session'
    # 构建表单数据
    data = {
        "commit": "Sign in",
        "authenticity_token": token,
        "login": "1941142883@qq.com",
        "password": "xbc1997525",
        "trusted_device": "",
        "webauthn-support": "supported",
        "webauthn-iuvpaa-support": "unsupported",
        "return_to": "https://github.com/login",
        "allow_signup": "",
        "client_id": "",
        "integration": "",
        "required_field_aafd": "",
        "timestamp": "1642061987490",
        "timestamp_secret": "b5dc2fada4219a92c8299ae2789c5f4370e0c6b3fdfe104938bbb82a6df0da84"
    }
    print(data)
    # 发送请求登录
    session.post(url2, data=data, headers=session.headers)

    # url3验证
    url3 = 'https://github.com/18326310729'
    response = session.get(url3)
    with open('github_session.html', 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    login()