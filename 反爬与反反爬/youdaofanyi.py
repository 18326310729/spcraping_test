import random
import requests
import hashlib
import time
import json


class Youdao(object):
    def __init__(self, word):
        self.url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1573484841@10.110.96.154; JSESSIONID=aaaSulTBDhSBP7Vu3Lk6x; OUTFOX_SEARCH_USER_ID_NCOO=46087759.16355821; ___rl__test__cookies=1643002737956',
            'Referer': 'https://fanyi.youdao.com/'
        }
        self.word = word
        self.formdata = None

    def generate_formdata(self):
        '''
            lts: "" + (new Date).getTime(),
            salt: ts + parseInt(10 * Math.random(), 10),
            sign: n.md5("fanyideskweb" + e + i + "Y2FYu%TNSbMCxc3t2u^XT")
        '''
        lts = str(int(time.time()*1000))
        salt = lts + str(random.randint(0, 9))
        tempstr = "fanyideskweb" + self.word + salt + "Y2FYu%TNSbMCxc3t2u^XT"
        md5 = hashlib.md5()
        md5.update(tempstr.encode())
        sign = md5.hexdigest()

        self.formdata = {
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "lts": lts,
            "bv": "866ddc825824adb95a25e4ff4107f5a0",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
            "i": self.word
        }

    def get_data(self):
        response = requests.post(self.url, data=self.formdata, headers=self.headers)
        return response.content

    def parse_data(self, data):
        dic_data = json.loads(data)

        print(dic_data['translateResult'][0][0]['tgt'])

    def run(self):
        self.generate_formdata()
        data = self.get_data()
        self.parse_data(data)


if __name__ == '__main__':
    youdao = Youdao('人生苦短')
    youdao.run()
