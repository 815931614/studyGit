
from threading import Thread,RLock
import time
import requests
from urllib.parse import urlencode
authorization_list = {
    '18986680202' : 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy5tYXJrYXJ0Z28uY29tL2FwaS9hdXRoL2xvZ2luUGFzcyIsImlhdCI6MTY2MjE4Nzg0NywiZXhwIjoxODc4MTg3ODQ3LCJuYmYiOjE2NjIxODc4NDcsImp0aSI6IkF2WUliaTZvaFI4SzRCQzgiLCJzdWIiOiIzMTU3OSIsInBydiI6ImY2NGQ0OGE2Y2VjN2JkZmE3ZmJmODk5NDU0YjQ4OGIzZTQ2MjUyMGEiLCJyb2xlIjoidXNlciJ9.WN96A4yFpyZwFCp5vCbUdkoM4tdx2TWTAwfmH1C52rc',
    '17683866129' : 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy5tYXJrYXJ0Z28uY29tL2FwaS9hdXRoL2xvZ2luUGFzcyIsImlhdCI6MTY2MjIwNDM3MCwiZXhwIjoxODc4MjA0MzcwLCJuYmYiOjE2NjIyMDQzNzAsImp0aSI6ImlycVlLM3I5Y2dFOUhkc04iLCJzdWIiOiIzMTcxNCIsInBydiI6ImY2NGQ0OGE2Y2VjN2JkZmE3ZmJmODk5NDU0YjQ4OGIzZTQ2MjUyMGEiLCJyb2xlIjoidXNlciJ9.TFRC09Q01Wm4YW9-pPveQwbdrhwTJJitNYLNoSkgktI'
}


class qianggou:


    def __init__(self,authorization_list):
        self.authorization_list = authorization_list
        self.createLock = RLock()
        self.isSuccess = {}
    def createThread(self):
        self.thread_list = []
        for i in  range(20):
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
        url = 'https://h5.ametays.art/api/nft.pay/pay'

        res = requests.post(url,
            headers={
                'Host': 'h5.ametays.art',
                'Connection': 'keep-alive',
                'Content-Length': '56',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                'XX-Device-Type': 'android',
                'app-client': 'wap',
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
                'token': '07fb097e-25ab-4b92-b39e-c4ade61382bb',
                'content-type': 'application/x-www-form-urlencoded',
                'Accept': '*/*',
                'Origin': 'https://h5.ametays.art',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://h5.ametays.art/web/',

            },
            data = urlencode({
                'pay_type' :'bank' ,
                'order_no': orderId,
                'paypassword': ""
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



        url = 'https://h5.ametays.art/api/nft.pay/addOrder'

        res = requests.post(url,
            headers={

                'Host': 'h5.ametays.art',
                'Connection': 'keep-alive',
                'Content-Length': '101',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                'XX-Device-Type': 'android',
                'app-client': 'wap',
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
                'token': '07fb097e-25ab-4b92-b39e-c4ade61382bb',
                'content-type': 'application/x-www-form-urlencoded',
                'Accept': '*/*',
                'Origin': 'https://h5.ametays.art',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://h5.ametays.art/web/',

            },
            data = urlencode({
                'order_token':'06e1c29e9723c0369bfd6deabc2f005c',
                'collection_id' : 24,
                'discount_type':'creation',
                'num' : 1,
                'scorePay': 0
            }),
            timeout=3,
            proxies=ip
         )
        '''
        {"code":1,"msg":"订单创建成功","time":"1662805808","data":{"user_id":8342,"order_no":"16628058089150220921","order_status":0,"order_type":1,"remarks":"","pay_status":0,"pay_price":"99.00","pay_limit_time":1662806408,"use_score":0,"before_buy_type":"","discount_type":"","discount_num":0,"goods_number":1,"created_at":1662805808,"updated_at":1662805808,"id":"7700","pay_limit_time_text":"2022-09-10 18:40:08","order_status_text":"待支付","prescription":"600"
        '''
        print(name,res.json())
        if res.json()['msg'] == "订单创建成功":

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

