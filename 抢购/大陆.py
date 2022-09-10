
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



        url = 'https://api.taohuan.life/api/cang/create'

        res = requests.post(url,
            headers={

                'Accept': '*/*',
                'app-id': '',
                'Cache-Control': 'no-cache',
                'client-type': 'H5',
                'Connection': 'keep-alive',
                'Content-Length': '467',
                'Content-Type': 'application/json',
                'Cookie': '__snaker__id=6BYh4cTyHE9D7Fwn; gdxidpyhxdE=mlzbU6now%2FTWTU3wRk3Y%5CbPCl7jE%2FeYdo2ViGgQXpNkWz11RJd2tZiY9ZUZEyf%5CDHysDkpCbc8wGN1iAYXfR5oOz5yaOO%5CW6oSdciXkmB03eQm%2F6KQekEtsfNQtuPy9GJjpa4nvfaZYB9MPnonc9plyBNn2QDocQDfnRNA%2BurghwGsCw%3A1662714447196; _9755xjdesxxd_=32; YD00385985691250%3AWM_NI=K%2BSBllz44hXfEootHVeaJx6mALQJ0lGekqcWjrOeH5qlEDRxCgaZvPdM5qfkev4cV00WaNRcJl0UJ6lbPi5%2Bly3fDV4FA3Extm8XHzU9EGDARMeIf4iunZ8Qd%2Bpl4NnHR3Y%3D; YD00385985691250%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee99b45cb1869fd9ca4fb3ac8ba6d14f978f9b83d44df3b58cb1ef7cacb1a2aeb42af0fea7c3b92a89f59da3ef68baecfc89db6e87b1a195cb5ea7bf8699b56783949fabb36885bba592e25daaae8186cb3fb3b48ba5d17481b9afbbf55ca893fb92e561a7aafc84d53cf489afafd1698ab400b6c93eb0bea08ab821b0a7fd87c75ef89a8fd4c874b8b3f8b9cb7297e78ba8c74b9293abaae540ababa2bbbb5ba8f5c08db746ae989ed4dc37e2a3; YD00385985691250%3AWM_TID=ka%2BZcTA7CgZAVEUQQFPBXwkGOwtl4mNw; token=eyJUeXBlIjoiSnd0IiwidHlwIjoiSldUIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiJTQUFTIiwianNvbkRhdGEiOiJ7XCJsb2dpblR5cGVcIjoxLFwidHlwZVwiOjMsXCJ1c2VySWRcIjpcIjEwNjA1MTEwMzI5Mzc5MjIwMDY2NDM3XCIsXCJ0ZW5hbnRJZFwiOlwiMTA2MTAwMTAwMDAwMDVcIn0iLCJleHAiOjE2NjMzMTg0MTR9.igBsxqnhyI2J_QTBaiQLhoSF4kdCgtWpdkwbTtf-pVY',
                'Host': 'xindalu-m.rarefy.cn',
                'nonce': '3WYYYwdIOQVFAYrj',
                'Origin': 'https://xindalu-m.rarefy.cn',
                'platform': 'H5',
                'Pragma': 'no-cache',
                'Referer': 'https://xindalu-m.rarefy.cn/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'signature': '9YaO6PO1iyeFQYhK3x_g6BvaLi9slsx50O_jM7bFpPU',
                'third-session': '',
                'timestamp': '1662724507779',
                'token': 'eyJUeXBlIjoiSnd0IiwidHlwIjoiSldUIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiJTQUFTIiwianNvbkRhdGEiOiJ7XCJsb2dpblR5cGVcIjoxLFwidHlwZVwiOjMsXCJ1c2VySWRcIjpcIjEwNjA1MTEwMzI5Mzc5MjIwMDY2NDM3XCIsXCJ0ZW5hbnRJZFwiOlwiMTA2MTAwMTAwMDAwMDVcIn0iLCJleHAiOjE2NjMzMTg0MTR9.igBsxqnhyI2J_QTBaiQLhoSF4kdCgtWpdkwbTtf-pVY',
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            },
            json = {
                "cardId":"10607210328962148819013",
                "id":"10605440329979443347589",
                "issueId":"10605440329979443347589",
                "multifileType":"image",
                "picUrl":"https://static.rarefy.cn/10610010000005/card/image1662449335882.png",
                "productId":"10607210328962148819013",
                "productName":"NL-Cyber Tiger",
                "productNo":"DmoZC718",
                "productType":0,
                "quantity":1,
                "salesPrice":300,
                "shopId":"106101296748347289733",
                "source":1,
                "userId":"10605110329379220066437",
                "orderSubType":1,
                "orderType":4,
                "userType":1
            },
            timeout=3,
            proxies=ip
         )
        '''
        https://xindalu-m.rarefy.cn/api/mallapp/toIssue/cardDetail?toIssueId=10605440329979443347589
        reqData: toIssueId=10605440329979443347589
        {"code":0,"msg":"成功","data":{"id":"10605440329979443347589","shopId":"106101296748347289733","title":"NL-Cyber Tiger","ossUrl":null,"publishType":4,"status":4,"totalNftCount":700,"residueNftCount":608,"chainChannelNoList":"100010","startTime":"2022-09-09 19:55:00","endTime":"2022-09-10 20:00:00","startTimeLong":1662724500000,"endTimeLong":1662811200000,"createTimeStamp":1662697789709,"publishTypeDesc":"特权购","shopName":"新大陆","shopHeadImgUrl":"https://static.rarefy.cn/10610010000005/card/image1654584709671.jpg","categoryName":null,"statusDesc":"上架中","card":{"cardId":"10607210328962148819013","cardName":"NL-Cyber Tiger","cardNo":"DmoZC718","ossUrl":"https://static.rarefy.cn/10610010000005/card/image1662449335882.png","ossUrlCompress":null,"multifileType":"image","subPicture":"","multfileCompress":null,"ipfsAddress":"QmW5Ri3cFf3EQ5B5n1FUg9wqZ8U65bT65TBfYhe8AufWtK","properties":"[{\"title\":\"新大陆\",\"content\":\"NL-Cyber Tiger\"}]","cardBenefit":"[]","chainChannelNo":"100010","royaltyRatio":500,"detailContent":"<p>NL-Cyber Tiger</p><p>“龙虎斗！我赢！”</p><p><img src=\"https://static.rarefy.cn/10610010000005/text/b972cdc8-b8d1-4bc4-a026-5788a77640a5.jpg\"></p>","count":1000},"price":300,"isSupportDonation":1,"donationCoolDown":1,"limitCount":2,"categoryNftFirstName":"新大陆","categoryNftSecondName":null,"buyType":2,"openMinute":5},"ok":true}
        
        '''


        print(name,res.json())
        # {"code":0,"msg":"成功","data":{"id":"120220909650330090082308165","shopId":"106101296748347289733","orderType":4,"orderSubType":4,"appId":null,"source":1,"userId":"10605110329379220066437","userType":2,"sellerId":null,"remark":null,"status":null,"payType":null,"payId":null,"payAmount":300,"fromUser":null,"toUser":null,"needPoll":false,"orderItemVo":{"shopId":"106101296748347289733","issueId":"10605440329979443347589","productId":"10607210328962148819013","productNo":"DmoZC718","productName":"NL-Cyber Tiger","cardId":"10607210328962148819013","cardNftId":null,"productType":0,"quantity":1,"salesPrice":300,"payAmount":null,"picUrl":"https://static.rarefy.cn/10610010000005/card/image1662449335882.png","multifileType":"image","isSupportDonation":1,"donationCoolDown":1}},"ok":true}
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

