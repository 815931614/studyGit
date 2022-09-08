
from threading import Thread,RLock
import time
import requests
from urllib.parse import urlencode
authorization_list = {
    # '18986680202' : '',
    '17683866129' : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjI2MjEzMTQsImlhdCI6MTY2MjUzNDkxNCwianRpIjoie1wibG9naW5UaW1lXCI6XCJXZWQgU2VwIDA3IDE1OjE1OjE0IENTVCAyMDIyXCIsXCJ1c2VySWRcIjpcIjM5ODUzM1wifSJ9.Cnfw4mZyVFvPJsfqRLGcv1W4UjDUpDiXITwi6-oFoNw'
}


class qianggou:


    def __init__(self,authorization_list):
        self.authorization_list = authorization_list
        self.createLock = RLock()
        self.isSuccess = {}
    def createThread(self):
        self.thread_list = []
        for i in  range(1):
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
        url = 'https://api.cqgmyyz.com/api/juh/openPay'

        res = requests.post(url,
            headers={

                'Accept': 'application/json, text/plain, */*',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Length': '24',
                'Content-Type': 'application/json',
                'Host': 'api.cqgmyyz.com',
                # 'meta-key': 'HTAXCwFqRZaP7Z7YarvJg3DXZZoUxdJJYB1A/krGcgnmwN/Tm2+W2o85uaDKuECUYsIL2PbGLag=',
                'Origin': 'https://h5.cqgmyyz.com',
                'Pragma': 'no-cache',
                'Referer': 'https://h5.cqgmyyz.com/',
                'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'token': authorization,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',

            },
            json = {"returnUrl":"https://h5.cqgmyyz.com/myBlindBox","failReturnUrl":"https://h5.cqgmyyz.com/order/buy","orderNo":orderId},
            timeout = 3,
            proxies = ip
        )
        '''
        {
	"code":"200",
	"data":"https://ledger.yftepay.com/pay/accountPaymentMethod?order_no=H22090715181288266370915&return_url=https://h5.cqgmyyz.com/order/buy&serviceName=dd02434a15cb4550ae6863f7cd618e2e",
	"msg":"success"
}
        
        '''
        if res.json()['msg'] == "success":
            print(name,res.json()['data'])
            return True
        print(name,res.json())
        return False

    def createOrder(self,authorization,name,ip):



        url = 'https://api.cqgmyyz.com/api/submitBlindBoxOrder'

        res = requests.post(url,
            headers={

                'Accept': 'application/json, text/plain, */*',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Length': '24',
                'Content-Type': 'application/json',
                'Host': 'api.cqgmyyz.com',
                # 'meta-key': 'HTAXCwFqRZaP7Z7YarvJg3DXZZoUxdJJYB1A/krGcgnmwN/Tm2+W2o85uaDKuECUYsIL2PbGLag=',
                'Origin': 'https://h5.cqgmyyz.com',
                'Pragma': 'no-cache',
                'Referer': 'https://h5.cqgmyyz.com/',
                'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'token': authorization,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',

            },
            json = {"id":"50","quantity":1},
            timeout=3,
            proxies=ip
         )
        '''
        {
            "code":"200",
            "data":{
                "amount":42.0,
                "deadlineTime":"2022-09-07 15:23:11",
                "orderNo":"202209071518118998224"
            },
            "msg":"success"
        }
        
        
        
        '''
        print(name,res.json())
        if res.json()['msg'] == "success":

            return res.json()['data']['orderNo']

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

