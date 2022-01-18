import requests
import json


class King(object):
    def __init__(self, word):
        self.url = 'http://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
        }
        self.data = {
            "from": "zh",
            "to": "en",
            "q": word
        }

    def get_data(self):
        response = requests.post(self.url, data=self.data, headers=self.headers)
        return response.content.decode()

    def parse_data(self, data):
        dic_data = json.loads(data)
        print(dic_data["content"]["out"])

    def run(self):
        res = self.get_data()
        print(res)
        self.parse_data(res)


if __name__ == '__main__':
    king = King('字典')
    king.run()
