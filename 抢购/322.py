
from threading import Thread,RLock
import time
import requests
from urllib.parse import urlencode
authorization_list = {
    '18986680202' : 'c02646ba-91aa-4ae2-a189-dd9084bfadc7',
    # '17683866129' : 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy5tYXJrYXJ0Z28uY29tL2FwaS9hdXRoL2xvZ2luUGFzcyIsImlhdCI6MTY2MjIwNDM3MCwiZXhwIjoxODc4MjA0MzcwLCJuYmYiOjE2NjIyMDQzNzAsImp0aSI6ImlycVlLM3I5Y2dFOUhkc04iLCJzdWIiOiIzMTcxNCIsInBydiI6ImY2NGQ0OGE2Y2VjN2JkZmE3ZmJmODk5NDU0YjQ4OGIzZTQ2MjUyMGEiLCJyb2xlIjoidXNlciJ9.TFRC09Q01Wm4YW9-pPveQwbdrhwTJJitNYLNoSkgktI'
}


class qianggou:


    def __init__(self,authorization_list):
        self.authorization_list = authorization_list
        self.createLock = RLock()
        self.isSuccess = {}
    def createThread(self):
        self.thread_list = []
        for i in  range(100):
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



        url = 'http://m.322meta.art/api/nft.pay/checkCollection?collection_id=104'

        res = requests.get(url,
            headers={
                'Accept': '*/*',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-type': 'application/json;charset=utf-8',
                'Host': 'm.322meta.art',
                'loginip': '16626978146985827946',
                'Pragma': 'no-cache',
                'Referer': 'http://m.322meta.art/h5/',
                'token': authorization,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            },

            timeout=3,
            proxies=ip
         )
        # {"code":0,"msg":"抢购暂未开始！","time":"1662698164","data":null}
        print(name,res.json())
        if res.json()['message'] == "下单成功":

            return res.json()['data']['order_no']

    def getIp(self):
        # url = 'http://api1.ydaili.cn/tools/BMeasureApi.ashx?action=BEAPI&secret=A93A19D427639C4C85BC8F1E0BE70F0CCF045BE529A547CCCEC1125E4A14B56C060AE56D7625D8AF&number=1&orderId=SH20220508203700211&format=txt'
        # ip = requests.get(url).text
        # print(ip.strip())
        return None
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

