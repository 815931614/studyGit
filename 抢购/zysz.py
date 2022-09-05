
from threading import Thread,RLock
import time
import requests
from urllib.parse import urlencode
authorization_list = {
    '15527254569' : 'MDAwMDAwMDAwMLFiprKTeLOjfqq_qLzOs2iChnPRvaWyqr-mvap_iH6YsGKqsYauyaJ_rayWsMuvsIGcc563fLtqso2lYoCMqNywhMSthoi6snzQ0aqvy6uvgaluow',
    # '17683866129' : 'MDAwMDAwMDAwML2apmyGnsywfr2smbCovKOAnILdvaLQZrKNqamLi3aYvJ22aJKLt6N-usCWsMuvsYKGlZ63fLtqs42pq4CiqNywhMSthoi6snzQ0aqvy6uvgaluow'
}


class qianggou:


    def __init__(self,authorization_list):
        self.authorization_list = authorization_list
        self.createLock = RLock()
        self.isSuccess = {}
    def createThread(self):
        self.thread_list = []
        for i in  range(2):
            for name,auth in self.authorization_list.items():
                self.isSuccess[name] = False
                t = Thread(target=self.run,args=(auth,name))
                t.start()
                self.thread_list.append(t)


    def run(self,authorization,name):

        while True:
            if int(time.time() * 1000) > 1662292795000:
                time.sleep(.01)
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


                'Accept': 'application/json, text/plain, */*',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Length': '13',
                'Content-Type': 'application/json',
                'Host': 'h5.zysz.art',
                'Origin': 'http://h5.zysz.art',
                'Pragma': 'no-cache',
                'Referer': 'http://h5.zysz.art/detail/9_1_0_0',
                'token': authorization,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',


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



        url = 'http://h5.zysz.art/api/market/opus/order/create'

        res = requests.post(url,
            headers={
                'Accept': 'application/json, text/plain, */*',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json',
                'Host': 'h5.zysz.art',
                'Origin': 'http://h5.zysz.art',
                'Pragma': 'no-cache',
                'Referer': 'http://h5.zysz.art/detail/9_1_0_0',
                'token': authorization,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            },
            timeout=3,
            proxies=ip,
            json={"opus_id":9}
         )

        print(name,res.json())

    def getIp(self):
        # url = 'http://api1.ydaili.cn/tools/BMeasureApi.ashx?action=BEAPI&secret=A93A19D427639C4C85BC8F1E0BE70F0CCF045BE529A547CCCEC1125E4A14B56C060AE56D7625D8AF&number=1&orderId=SH20220508203700211&format=txt'
        # ip = requests.get(url).text
        # print(ip.strip())
        return None
        # return {
        #     "https":  ip.strip(),
        #     "http":  ip.strip()
        # }

if __name__ == '__main__':


    a = qianggou(authorization_list)

    # print(a.getIp())

    a.createThread()

    while True:
        time.sleep(2222)

