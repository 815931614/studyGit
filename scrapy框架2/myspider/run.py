'''
Author: 815931614 815931614@qq.com
Date: 2022-08-31 14:22:26
LastEditors: 815931614 815931614@qq.com
LastEditTime: 2022-08-31 14:27:34
FilePath: \MyNote\scrapy框架2\myspider\run.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from scrapy import cmdline

cmdline.execute('scrapy crawl itcast'.split())