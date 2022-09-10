
from threading import Thread,RLock
import time
import requests
from urllib.parse import urlencode
authorization_list = {
    '000000' : 'ba733790f2854341810d2d24a1058d7a',
    # '123456' : 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy5tYXJrYXJ0Z28uY29tL2FwaS9hdXRoL2xvZ2luUGFzcyIsImlhdCI6MTY2MjIwNDM3MCwiZXhwIjoxODc4MjA0MzcwLCJuYmYiOjE2NjIyMDQzNzAsImp0aSI6ImlycVlLM3I5Y2dFOUhkc04iLCJzdWIiOiIzMTcxNCIsInBydiI6ImY2NGQ0OGE2Y2VjN2JkZmE3ZmJmODk5NDU0YjQ4OGIzZTQ2MjUyMGEiLCJyb2xlIjoidXNlciJ9.TFRC09Q01Wm4YW9-pPveQwbdrhwTJJitNYLNoSkgktI'
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
        url = 'http://121.196.174.25:8400/Home/Payorder'

        res = requests.post(url,
            headers={

                'Accept': '*/*',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Length': '7',
                'Content-Type': 'application/x-www-form-urlencoded',
                'header': '[object Object]',
                'Host': '121.196.174.25:8400',
                'Origin': 'http://hjkj68.com',
                'Pragma': 'no-cache',
                'Referer': 'http://hjkj68.com/',
                'token': 'authorization',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',

            },
            data = urlencode({
                'id': orderId[1],
                'type': 1,
                'password': name
            }),
            timeout = 3,
            proxies = ip
        )
        print(name, res.json())
        if res.json()['message'] == "支付成功":
            print(name,res.json()['data']['url'])
            return True

        return False

    def createOrder(self,authorization,name,ip):

        '''

get             Time: function() {
                    var t = new Date
                      , i = t.getFullYear()
                      , e = t.getMonth() + 1
                      , n = t.getDate()
                      , a = t.getHours() < 10 ? "0" + t.getHours() : t.getHours()
                      , o = t.getMinutes() < 10 ? "0" + t.getMinutes() : t.getMinutes()
                      , s = t.getSeconds() < 10 ? "0" + t.getSeconds() : t.getSeconds();
                    e >= 1 && e <= 9 && (e = "0" + e),
                    n >= 0 && n <= 9 && (n = "0" + n),
                    this.time = i + "-" + e + "-" + n + " " + a + ":" + o + ":" + s,
                    this.detailno = i + e + n + a + o + s + Math.floor(1e6 * Math.random() + 1)
                }

        20220909125431769418
sellTime  1662702295000
        :param authorization:
        :param name:
        :param ip:
        :return:
        '''
        order_no = time.strftime("%Y%m%d%H%M%S") + str(int(time.time()*1000))[-7:-1]
        url = 'http://121.196.174.25:8400/Home/Confirmorder'

        res = requests.post(url,
            headers={

                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Length': '7',
                'Content-Type': 'application/x-www-form-urlencoded',
                'header': '[object Object]',
                'Host': '121.196.174.25:8400',
                'Origin': 'http://hjkj68.com',
                'Pragma': 'no-cache',
                'Referer': 'http://hjkj68.com/',
                'token': authorization,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',

            },
            data = urlencode({
                'id': 73,
                'orderno': order_no
            }),
            timeout=3,
            proxies=ip
         )

        print(name,res.json())
        if res.json()['info'] == "处理成功！":

            return order_no,res.json()['data']

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

