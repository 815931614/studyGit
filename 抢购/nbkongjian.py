
from threading import Thread,RLock
import time
import requests
from urllib.parse import urlencode
authorization_list = {
    '371063' : '36e7173b45d41df8f0bb377fc0bf2e39',
    '200472' : '5d23b83d6b1089de537e9fefc949d728'
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

        while True:
            if int(time.time() * 1000) > 1662206395000:
                time.sleep(.1)
                break
        ip = self.getIp()
        orderId = None

        while not self.isSuccess[name]:
            try:
                # 1662206770930561  1662206770549568  1662206781243549  1662206785847380
                orderId = self.createOrder(authorization,name,ip)
                if orderId:
                   self.isSuccess['name'] = True
                   while True:
                       try:
                           extractPayLink = self.extractPayLink(orderId, authorization,name,ip)
                           if extractPayLink:
                               break
                       except:
                           ip = self.getIp()
                   break
            except:
                ip = self.getIp()



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



        url = 'https://api.nbkongjian.com/index.php?s=/api/Checkout/orders'

        res = requests.post(url,
            headers={
                'Accept': '*/*',
                'Access-Token': authorization,
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Length': '67',
                'Content-Type': 'application/json',
                'Host': 'api.nbkongjian.com',
                'Origin': 'http://h5.nbkongjian.com',
                'platform': 'H5',
                'Pragma': 'no-cache',
                'Referer': 'http://h5.nbkongjian.com/',
                'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'cross-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            },
            json = {"goodsid":83,"userid":name,"isBox":0,"pay_type":30,"goodssum":1},
            timeout=3,
            proxies=ip
         )

        print(name,res.json())
        if res.json()['message'] == "下单成功":

            return res.json()['data']['order_no']

    def getIp(self):
        url = 'http://api1.ydaili.cn/tools/BMeasureApi.ashx?action=BEAPI&secret=A93A19D427639C4C85BC8F1E0BE70F0CCF045BE529A547CCCEC1125E4A14B56C060AE56D7625D8AF&number=1&orderId=SH20220508203700211&format=txt'
        ip = requests.get(url).text
        print(ip.strip())
        # return None
        return {
            "https":  ip.strip(),
            "http":  ip.strip()
        }

if __name__ == '__main__':


    a = qianggou(authorization_list)

    # print(a.getIp())

    a.createThread()

    while True:
        time.sleep(2222)

