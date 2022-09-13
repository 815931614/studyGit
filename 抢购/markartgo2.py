
from threading import Thread,RLock
import time
import requests
from urllib.parse import urlencode
from copy import deepcopy
authorization_list = {
    '18986680202' : 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy5tYXJrYXJ0Z28uY29tL2FwaS9hdXRoL2xvZ2luUGFzcyIsImlhdCI6MTY2Mjk3MzkzNywiZXhwIjoxODc4OTczOTM3LCJuYmYiOjE2NjI5NzM5MzcsImp0aSI6Im1wdTd5Q1RMckRhTEdhTDIiLCJzdWIiOiIzMTU3OSIsInBydiI6ImY2NGQ0OGE2Y2VjN2JkZmE3ZmJmODk5NDU0YjQ4OGIzZTQ2MjUyMGEiLCJyb2xlIjoidXNlciJ9.0iG16I180hYUJjt-OuCLTAa8WEmJt4u5GsEweU50d28',
    # '17683866129' : 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy5tYXJrYXJ0Z28uY29tL2FwaS9hdXRoL2xvZ2luUGFzcyIsImlhdCI6MTY2MjIwNDM3MCwiZXhwIjoxODc4MjA0MzcwLCJuYmYiOjE2NjIyMDQzNzAsImp0aSI6ImlycVlLM3I5Y2dFOUhkc04iLCJzdWIiOiIzMTcxNCIsInBydiI6ImY2NGQ0OGE2Y2VjN2JkZmE3ZmJmODk5NDU0YjQ4OGIzZTQ2MjUyMGEiLCJyb2xlIjoidXNlciJ9.TFRC09Q01Wm4YW9-pPveQwbdrhwTJJitNYLNoSkgktI'
}

order_list = {
    '18986680202' : ['1202209121714074510598144'],
    '17683866129' : []
}

class qianggou:


    def __init__(self,authorization_list,order_list):
        self.authorization_list = authorization_list
        self.createLock = RLock()
        self.isSuccess = {}
        self.orderList = order_list

    def createThread(self):
        self.thread_list = []

        for name,auth in self.authorization_list.items():
            self.isSuccess[name] = False
            t = Thread(target=self.run,args=(auth,name))
            t.start()
            self.thread_list.append(t)


    def run(self,authorization,name):
        ip = self.getIp()
        while True:
            try:
                for order  in deepcopy(self.orderList[name]):
                    extractPayLink = self.extractPayLink(order, authorization,name,ip)
                    if extractPayLink:
                        self.orderList[name].remove(order)
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
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
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
    def showOrder(self,authorization,name,ip):

        url = 'https://www.markartgo.com/api/my/order?status=1&page=1&size=10'

        res = requests.get(url,
            headers={

                'accept': '*/*',
                'authorization': authorization,
                'cache-control': 'no-cache',
                'origin': 'http://h5.markartgo.com',
                'pragma': 'no-cache',
                'referer': 'http://h5.markartgo.com/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            },
            timeout=3,
            proxies=ip
         )

        print(name,name,res.json())





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


    a = qianggou(authorization_list,order_list)

    # print(a.getIp())

    # a.createThread()

    while True:
        try:
            a.showOrder(authorization_list['17683866129'], "", None)
            a.showOrder(authorization_list['18986680202'], "", None)
        except:
            pass

