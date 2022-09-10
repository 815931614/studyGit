# coding:utf-8
"""
@Project ：MyNote 
@File    ：zz.py
@IDE     ：PyCharm 
@Author  ：lifucheng
@Date    ：2022/9/10 13:03
"""

import requests
import time


6213

res = requests.get("http://client.kfdm.cn/api/mine/collect?curPage=1&limit=100&ipId=41&ipTypeId=&q=",
               headers={
                    'Accept': '*/*',
                    'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzOTA3NSIsImV4cCI6MTY2NTM3ODE1OSwiaWF0IjoxNjYyNzg2MTU5fQ.IG0CZ9GOLnR8-lzRhI7stIzRQr_8a_cugHMN4x8K2xY',
                    'Cache-Control': 'no-cache',
                    'Connection': 'keep-alive',
                    'Host': 'client.kfdm.cn',
                    'Origin': 'http://h5.kfdm.cn',
                    'Pragma': 'no-cache',
                    'Referer': 'http://h5.kfdm.cn/',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
               })
print(len(res.json()['data']['list']))

for l in res.json()['data']['list']:
    res = requests.post(f'http://client.kfdm.cn/api/mine/collect/{l["id"]}/donate/6213/bcb15f821479b4d5772bd0ca866c00ad5f926e3580720659cc80d39c9d09802a',

                        headers = {
                            'Accept': '*/*',
                            'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzOTA3NSIsImV4cCI6MTY2NTM3ODE1OSwiaWF0IjoxNjYyNzg2MTU5fQ.IG0CZ9GOLnR8-lzRhI7stIzRQr_8a_cugHMN4x8K2xY',
                            'Cache-Control': 'no-cache',
                            'Connection': 'keep-alive',
                            'Content-Length': '2',
                            'content-type': 'application/json',
                            'Host': 'client.kfdm.cn',
                            'Origin': 'http://h5.kfdm.cn',
                            'Pragma': 'no-cache',
                            'Referer': 'http://h5.kfdm.cn/',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                        },
                        json={}


    )
    print(res.json())
