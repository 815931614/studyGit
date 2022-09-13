
from threading import Thread,RLock
import time
import requests
from urllib.parse import urlencode
authorization_list = {
    '18986680202' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLnRhb2h1YW4ubGlmZVwvYXBpXC91c2VyXC9sb2dpbiIsImlhdCI6MTY2MjQ0Mjk1MSwibmJmIjoxNjYyNDQyOTUxLCJqdGkiOiJLUlViYlZ6OUh0NXh1N2VVIiwic3ViIjozMTgyMSwicHJ2IjoiODdlMGFmMWVmOWZkMTU4MTJmZGVjOTcxNTNhMTRlMGIwNDc1NDZhYSJ9.7cHeKTGkaZvLxEt1R3wYmLcBf3305ZU2osRhJZcO14c',
    '17683866129' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLnRhb2h1YW4ubGlmZVwvYXBpXC91c2VyXC9sb2dpbiIsImlhdCI6MTY2MjYxOTYxMCwibmJmIjoxNjYyNjE5NjEwLCJqdGkiOiI1aEcwcnQ4enpyS3JYeVZiIiwic3ViIjo5NjM5LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.sBoc48OA0MchhiXTr1KZpK6DzLEiWi5dZ80pHFk_MIQ'
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
            if int(time.time() * 1000) > 1662620395000:
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



        url = 'https://art.jinyuanshucang.com/api/order/add'
        '''
        https://art.jinyuanshucang.com/api/order/box
        {"goods_id":107,"pay_type":"1"}
        '''
        res = requests.post(url,
            headers={

                'accept': '*/*',
                'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJyZWRsayIsImV4cCI6MTY2NDA5NjMzNSwiYXVkIjoicmVkbGsiLCJuYmYiOjE2NjI4MDAzMzUsImlhdCI6MTY2MjgwMDMzNSwidWlkIjoxMDAwMTI5NTMsInR5cGUiOjF9.UAx2sRc-BLGwAkL2xEVP3o4MmxCjnwP8xDTCfPBhnyg',
                'cache-control': 'no-cache',
                'content-length': '30',
                'content-type': 'application/json',
                'origin': 'https://web.jinyuanshucang.com',
                'os': 'windows',
                'pragma': 'no-cache',
                'referer': 'https://web.jinyuanshucang.com/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
                'version': 'undefined',
                'versioncode': 'undefined',
            },
            json = {"goods_id":96,"pay_type":"1"},
            timeout=3,
            proxies=ip
         )
        # {"status_code":200,"data":"https:\/\/sandcash.mixienet.com.cn\/pay\/h5\/quicktopup?version=10&mer_no=6888806046047&mer_key=8TUMCGZGegbofbduWflXVl2SpwlR7ywQ968oUipjqCQzYC3Ka0bNb51fMAQndy7pKJiIBlHO55s%3D&mer_order_no=2022090613260234895&create_time=20220906132602&expire_time=20220906135602&order_amt=1.00&notify_url=https%3A%2F%2Fweb.taohuan.life%2Fnotify%2Fsdpay&return_url=https%3A%2F%2Fweb.taohuan.life%2Fnotify%2Fpaysuccess&create_ip=117.152.93.117&goods_name=%E5%95%86%E5%93%81%E8%B4%AD%E4%B9%B0&store_id=000000&product_code=06030003&clear_cycle=3&pay_extra=%7B%22userId%22%3A%2231087%22%2C%22userName%22%3A%22%5Cu674e%5Cu798f%5Cu6210%22%2C%22idCard%22%3A%22421003199906082911%22%7D&accsplit_flag=NO&jump_scheme=sandcash%3A%2F%2Fscpay&meta_option=%5B%7B%22s%22%3A%22Android%22%2C%22n%22%3A%22wxDemo%22%2C%22id%22%3A%22com.pay.paytypetest%22%2C%22sc%22%3A%22com.pay.paytypetest%22%7D%5D&sign_type=MD5&sign=5DF93FDA9399AB5210EB831F196CB1D9","message":"https:\/\/sandcash.mixienet.com.cn\/pay\/h5\/quicktopup?version=10&mer_no=6888806046047&mer_key=8TUMCGZGegbofbduWflXVl2SpwlR7ywQ968oUipjqCQzYC3Ka0bNb51fMAQndy7pKJiIBlHO55s%3D&mer_order_no=2022090613260234895&create_time=20220906132602&expire_time=20220906135602&order_amt=1.00&notify_url=https%3A%2F%2Fweb.taohuan.life%2Fnotify%2Fsdpay&return_url=https%3A%2F%2Fweb.taohuan.life%2Fnotify%2Fpaysuccess&create_ip=117.152.93.117&goods_name=%E5%95%86%E5%93%81%E8%B4%AD%E4%B9%B0&store_id=000000&product_code=06030003&clear_cycle=3&pay_extra=%7B%22userId%22%3A%2231087%22%2C%22userName%22%3A%22%5Cu674e%5Cu798f%5Cu6210%22%2C%22idCard%22%3A%22421003199906082911%22%7D&accsplit_flag=NO&jump_scheme=sandcash%3A%2F%2Fscpay&meta_option=%5B%7B%22s%22%3A%22Android%22%2C%22n%22%3A%22wxDemo%22%2C%22id%22%3A%22com.pay.paytypetest%22%2C%22sc%22%3A%22com.pay.paytypetest%22%7D%5D&sign_type=MD5&sign=5DF93FDA9399AB5210EB831F196CB1D9"}
        print(name,res.json())
        # if res.json()['message'] == "下单成功":
        #
        #     return res.json()['data']['order_no']

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

