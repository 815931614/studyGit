
from threading import Thread,RLock
import time
import requests
from urllib.parse import urlencode
from copy import deepcopy
authorization_list = {
    '18986680202' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLnRhb2h1YW4ubGlmZVwvYXBpXC91c2VyXC9sb2dpbiIsImlhdCI6MTY2MjQ0Mjk1MSwibmJmIjoxNjYyNDQyOTUxLCJqdGkiOiJLUlViYlZ6OUh0NXh1N2VVIiwic3ViIjozMTgyMSwicHJ2IjoiODdlMGFmMWVmOWZkMTU4MTJmZGVjOTcxNTNhMTRlMGIwNDc1NDZhYSJ9.7cHeKTGkaZvLxEt1R3wYmLcBf3305ZU2osRhJZcO14c',
    '17683866129' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLnRhb2h1YW4ubGlmZVwvYXBpXC91c2VyXC9sb2dpbiIsImlhdCI6MTY2MjYxOTYxMCwibmJmIjoxNjYyNjE5NjEwLCJqdGkiOiI1aEcwcnQ4enpyS3JYeVZiIiwic3ViIjo5NjM5LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.sBoc48OA0MchhiXTr1KZpK6DzLEiWi5dZ80pHFk_MIQ'
}

order_list = {
    '18986680202' : [],
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
        url = 'https://api.taohuan.life/api/cang/payorder'

        res = requests.post(url,
            headers={
                'accept': '*/*',
                'authorization': authorization,
                'cache-control': 'no-cache',
                'content-length': '333',
                'content-type': 'application/json',
                'origin': 'https://web.taohuan.life',
                'platform': 'h5',
                'pragma': 'no-cache',
                'referer': 'https://web.taohuan.life/',
                'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            },
            json ={"id":orderId,"pay_type":"SDKJ"},
            timeout = 3,
            proxies = ip
        )

        if res.json()['message'] == "支付成功":
            print(name,res.json()['data']['url'])
            return True
        print(name,res.json())
        return False
    def showOrder(self,authorization,name,ip):

        url = 'https://api.taohuan.life/api/manghe/orderlist'

        res = requests.post(url,
            headers={

                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9',
                'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLnRhb2h1YW4ubGlmZVwvYXBpXC91c2VyXC9sb2dpbiIsImlhdCI6MTY2MjQ0MTg4MywibmJmIjoxNjYyNDQxODgzLCJqdGkiOiJGcUlTSlpPYkwzNjNaMERPIiwic3ViIjozMTA4NywicHJ2IjoiODdlMGFmMWVmOWZkMTU4MTJmZGVjOTcxNTNhMTRlMGIwNDc1NDZhYSJ9.GiV0HpeIVgKm81hFBAfgg39o1ia7nd967Sj9_M33oew',
                'cache-control': 'no-cache',
                'content-length': '333',
                'content-type': 'application/json',
                'origin': 'https://web.taohuan.life',
                'platform': 'h5',
                'pragma': 'no-cache',
                'referer': 'https://web.taohuan.life/',
                'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',

            },
            json={"status":0,"page":1},
            timeout=3,
            proxies=ip
        )
        # if res['data'] =
        '''
        {"current_page":1,"data":[],"first_page_url":"https:\/\/api.taohuan.life\/api\/manghe\/orderlist?page=1","from":null,"last_page":1,"last_page_url":"https:\/\/api.taohuan.life\/api\/manghe\/orderlist?page=1","next_page_url":null,"path":"https:\/\/api.taohuan.life\/api\/manghe\/orderlist","per_page":10,"prev_page_url":null,"to":null,"total":0}
        {"current_page":1,"data":[{"id":"2022090613260284199","user_id":31087,"status":0,"price":"1.00","type":1,"created_at":"2022-09-06 13:26:02","updated_at":"2022-09-06 13:26:02","pic_url":"https:\/\/image.taohuan.life\/images\/\u4e2d\u79cb\u7cfb\u521701.png","good_title":"\u5bb6\u597d\u6708\u5706-\u5ae6\u5a25","pay_type":0,"remainingTime":922}],"first_page_url":"https:\/\/api.taohuan.life\/api\/manghe\/orderlist?page=1","from":1,"last_page":1,"last_page_url":"https:\/\/api.taohuan.life\/api\/manghe\/orderlist?page=1","next_page_url":null,"path":"https:\/\/api.taohuan.life\/api\/manghe\/orderlist","per_page":10,"prev_page_url":null,"to":1,"total":1}
        '''


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



    while True:
        try:
            a.showOrder(authorization_list['17683866129'], "", None)
            a.showOrder(authorization_list['18986680202'], "", None)
        except:
            pass

