'''
Author: 815931614 815931614@qq.com
Date: 2022-09-01 01:19:03
LastEditors: 815931614 815931614@qq.com
LastEditTime: 2022-09-01 01:20:07
FilePath: \MyNote\scrapy框架2\cf.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE



'''
def cookie_to_dic(cookie):
  return {item.split('=')[0]: item.split('=')[1] for item in cookie.split('; ')}



print(cookie_to_dic('ll="118254"; bid=IHGkoqBDJKM; __utmc=30149280; __utmz=30149280.1661951058.1.json.1.json.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _ga=GA1.1.json.1538874449.1661951058; __gads=ID=6aa603e6feb38aac-22d07d9a14d60003:T=1661951064:RT=1661951064:S=ALNI_MZmW5cQqYrv3YH49h2rGWKXhKCOyA; __gpi=UID=0000094f796b4c3d:T=1661951064:RT=1661951064:S=ALNI_MZL2sxObDadwLzISKyGFhSHH9TF3w; gr_user_id=782b93b5-b964-482b-a938-8f1c27e1c013; __utmc=81379588; __utmz=81379588.1661951554.1.json.1.json.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=DA38A8464D7EBD54ED996DF06110FD7E2|49f9176ca438d603eaf6515550d283b8; __yadk_uid=JCve9d0WCFue9LK9rsi8CYEIldRKP7UA; _ga_RXNMP372GL=GS1.1.json.1661951061.1.json.1.json.1661952048.22.0.0; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1661958961%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.3ac3=*; __utma=30149280.1538874449.1661951058.1661951058.1661958961.2; __utma=81379588.1538874449.1661951058.1661951554.1661958961.2; viewed="4913064_35517022_30396222_35886207_35587028_35658993"; dbcl2="168282384:Lm19wc1r9/E"; ck=TZzU; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=9e7d993a-fb91-41c6-9efd-99d6d2c6d672; gr_cs1_9e7d993a-fb91-41c6-9efd-99d6d2c6d672=user_id%3A1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_9e7d993a-fb91-41c6-9efd-99d6d2c6d672=true; push_noty_num=0; push_doumail_num=0; __utmt_douban=1.json; __utmt=1.json; _pk_id.100001.3ac3=f54566227e6602f5.1661951554.2.1661966369.1661953599.; __utmb=30149280.34.10.1661958961; __utmb=81379588.34.10.1661958961'))