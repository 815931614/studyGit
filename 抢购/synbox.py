
from threading import Thread,RLock
import time
import requests
from urllib.parse import urlencode
import hashlib
import traceback
authorization_list = {
    '18986680202' : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6Ik1JTkdZQU5HQjdEMEM5RDI3OTg5Mjg1N0RFNTQ5MEFCODU2NzcyRkUifQ.eyJpc3MiOiJodHRwczpcL1wvd3d3Lm15enkuY29tLmNuIiwiYXVkIjoiaHR0cHM6XC9cL3d3dy5teXp5LmNvbS5jbiIsImp0aSI6Ik1JTkdZQU5HQjdEMEM5RDI3OTg5Mjg1N0RFNTQ5MEFCODU2NzcyRkUiLCJpYXQiOjE2NjIzNjYyNDEsIm5iZiI6MTY2MjM2NjI0MSwiZXhwIjoxNjYyMzY5ODQxLCJ1dWlkIjo5NzY5NywiY2xpZW50X3R5cGUiOjF9.A2W99D1kbXUeF1M1N68FQzsGwkUvWDlXSFv8Xyoez6M',
    '17683866129' : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6Ik1JTkdZQU5HQjdEMEM5RDI3OTg5Mjg1N0RFNTQ5MEFCODU2NzcyRkUifQ.eyJpc3MiOiJodHRwczpcL1wvd3d3Lm15enkuY29tLmNuIiwiYXVkIjoiaHR0cHM6XC9cL3d3dy5teXp5LmNvbS5jbiIsImp0aSI6Ik1JTkdZQU5HQjdEMEM5RDI3OTg5Mjg1N0RFNTQ5MEFCODU2NzcyRkUiLCJpYXQiOjE2NjIzNjMyMzgsIm5iZiI6MTY2MjM2MzIzOCwiZXhwIjoxNjYyMzY2ODM4LCJ1dWlkIjo5NjQ5NywiY2xpZW50X3R5cGUiOjF9.q1iUjqS4wCypdRK37HXRoCQFzkQZxHLbd7r3tIhFnd4'
}


class qianggou:


    def __init__(self,authorization_list):
        self.authorization_list = authorization_list
        self.createLock = RLock()
        self.isSuccess = {}
    def createThread(self):
        self.thread_list = []
        for i in  range(10):
            for name,auth in self.authorization_list.items():
                self.isSuccess[name] = False
                t = Thread(target=self.run,args=(auth,name))
                t.start()
                self.thread_list.append(t)


    def run(self,authorization,name):

        # while True:
        #     if int(time.time() * 1000) > 1662371995000:
        #         time.sleep(.1)
        #         break
        ip = self.getIp()
        orderId = None

        while not self.isSuccess[name]:
            try:
                # 1662206770930561  1662206770549568  1662206781243549  1662206785847380
                orderId = self.createOrder(authorization,name,ip)
                # if orderId:
                #    self.isSuccess['name'] = True
                #    break
            except:
                # traceback.print_exc()
                ip = self.getIp()

    def USE_MD5(self,test):
        if not isinstance(test, bytes):
            test = bytes(test, 'utf-8')
        m = hashlib.md5()
        m.update(test)
        return m.hexdigest()


    def extractPayLink(self,orderId,authorization,name,ip):
        url = 'https://www.markartgo.com/api/sd/sdNewQuick'

        res = requests.post(url,
            headers={
                'Accept': '*/*',
                'Authorization': authorization,
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Host': 'www.markartgo.com',
                'Origin': 'http://h5.markartgo.com',
                'Pragma': 'no-cache',
                'Referer': 'http://h5.markartgo.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'cross-site',
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.json.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1.json',

            },
            data = urlencode({
                "order_no": orderId,
            }),
            timeout = 3,
            proxies = ip
        )

        if res.json()['message'] == "支付成功":
            print(name,res.json()['data']['url'])
            return True
        print(name,res.json())
        return False

    def createOrder(self,authorization,name,ip):



        url = 'https://nft.synbox.cn/v1/createOrder'
        timestamp = int(time.time() * 1000)
        sign =self.USE_MD5(f'domain=https://nft.synbox.cn/&goods_num=1&key=MINGYANGB7D0C9D279892857DE5490AB856772FE&ordertype=0&pathinfo=v1/createOrder&paytype=quickPay&special_id=188&timestamp={timestamp}')
        res = requests.post(url,
            headers={

                'Accept': '*/*',
                'Cache-Control': 'no-cache',
                'content-type': 'application/json;charset=UTF-8',
                'debug': 'false',
                'Host': 'nft.synbox.cn',
                'Origin': 'https://nft.synbox.cn',
                'Pragma': 'no-cache',
                'Referer': 'https://nft.synbox.cn/H5/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'sign': sign,
                'timestamp': str(timestamp),
                'token': authorization,
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',            },
            json = {"special_id":"188","paytype":"quickPay","ordertype":0,"goods_num":1},
            timeout=10,
            proxies=ip
         )

        print(name,res.json())
        if res.json()['data']:

            return res.json()['data']['order_no']

    def getIp(self):
        # url = 'http://api1.ydaili.cn/tools/BMeasureApi.ashx?action=BEAPI&secret=A93A19D427639C4C85BC8F1E0BE70F0CCF045BE529A547CCCEC1125E4A14B56C060AE56D7625D8AF&number=1&orderId=SH20220508203700211&format=txt'
        # ip = requests.get(url).text
        # print(ip.strip())
        return None
        # return {
        #     "https":  ip.strip(),
        #     "http":  ip.strip()
        # }
        '''
        
        https://ledger.yftepay.com/bankCardPay/pay?order_no=
        
        '''

if __name__ == '__main__':


    a = qianggou(authorization_list)

    # print(a.getIp())

    a.createThread()

    while True:
        time.sleep(2222)

