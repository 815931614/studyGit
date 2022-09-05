'''
Author: 815931614 815931614@qq.com
Date: 2022-08-31 23:02:37
LastEditors: 815931614 815931614@qq.com
LastEditTime: 2022-09-01 01:44:53
FilePath: \MyNote\scrapy框架2\scrapy_shell.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 impor
'''

$ scrapy shell
...
...
>>> from scrapy import Request
>>> req = Request('https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4', headers={    
    'user-agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
},cookies = {'ll': '"118254"', 'bid': 'IHGkoqBDJKM', '__utmc': '81379588', '__utmz': '81379588.1661951554.1.1.utmcsr', '_ga': 'GA1.1.1538874449.1661951058', '__gads': 'ID', '__gpi': 'UID', 'gr_user_id': '782b93b5-b964-482b-a938-8f1c27e1c013', '_vwo_uuid_v2': 'DA38A8464D7EBD54ED996DF06110FD7E2|49f9176ca438d603eaf6515550d283b8', '__yadk_uid': 'JCve9d0WCFue9LK9rsi8CYEIldRKP7UA', '_ga_RXNMP372GL': 'GS1.1.1661951061.1.1.1661952048.22.0.0', '_pk_ref.100001.3ac3': '%5B%22%22%2C%22%22%2C1661958961%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D', '_pk_ses.100001.3ac3': '*', '__utma': '81379588.1538874449.1661951058.1661951554.1661958961.2', 
            'viewed': '"4913064_35517022_30396222_35886207_35587028_35658993"', 'dbcl2': '"168282384:Lm19wc1r9/E"', 'ck': 'TZzU', 'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03': '9e7d993a-fb91-41c6-9efd-99d6d2c6d672', 'gr_cs1_9e7d993a-fb91-41c6-9efd-99d6d2c6d672': 'user_id%3A1', 'gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_9e7d993a-fb91-41c6-9efd-99d6d2c6d672': 'true', 'push_noty_num': '0', 'push_doumail_num': '0', '__utmt_douban': '1', '__utmt': '1', '_pk_id.100001.3ac3': 'f54566227e6602f5.1661951554.2.1661966369.1661953599.', '__utmb': '81379588.34.10.1661958961'}
)

>>> fetch(req)
li_list = re.xpath('//*[@id="info"]/text()')
