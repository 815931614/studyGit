# coding:utf-8
"""
@Project ：MyNote 
@File    ：bilibili.py
@IDE     ：PyCharm 
@Author  ：lifucheng
@Date    ：2022/9/11 17:55
"""

from chrome import BaseChrome
from selenium.webdriver.common.action_chains import  ActionChains
import logging,re,time,random,requests
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    datefmt='%Y:%m:%d %H:%M:%S',
                    )

logger = logging.getLogger()

class Bilibili:


    def __init__(self):
        self.basechrom = BaseChrome(executable_path=r'D:\chrome-win\chromedriver')
        self.driver = self.basechrom.driver



    def home(self):
        self.basechrom.get('https://www.bilibili.com/')
        # self.basechrom.new_window('https://www.bilibili.com/')


    def show_login_window(self):
        # 打开登录窗口
        login_btn = self.basechrom.find_element(value='//div[@class="login-btn"]')
        if login_btn:
            login_btn.click()
            return True
        else:
            logger.error(': 登录窗口打开失败')



    def username_passwor_login(self,username,password):
        # 输入账号密码
        username_input = self.basechrom.find_element(value='/html/body/div[3]/div/div[2]/div[3]/div[2]/div[1]/input')
        password_input = self.basechrom.find_element(value='/html/body/div[3]/div/div[2]/div[3]/div[2]/div[2]/div[1]/input')
        if username_input and password_input:
            username_input.send_keys(username)
            password_input.send_keys(password)
        else:
            logger.error(': 未找到登录输入框')
            return None


        # 点击登录按钮
        self.basechrom.find_element(value='/html/body/div[3]/div/div[2]/div[3]/div[3]/div[2]').click()


        # 通过元素style中display值判断验证码是否以显示
        div = self.basechrom.find_element(value='/html/body/div[4]').get_attribute('style')
        print(div) # display: block; opacity: 1;
        if 'block' not in div:
            logger.error(': 未找到验证码图片')
            return None



        # 方式一：获取验证码图片url地址，下载图片
        # div = self.basechrom.find_element(value='/html/body/div[4]/div[2]/div[6]/div/div/div[2]/div[1]/div/div[2]').get_attribute('style')
        # url = re.findall(r'url\("(.*?)"\);',div)[0]
        # 下载图片
        # with open('capth.png','wb') as w:
        #     w.write(requests.get(url).content)



        # 方式二：通过节点截取图片
        min_img = self.basechrom.find_element('/html/body/div[4]/div[2]/div[6]/div/div/div[1]/div[1]/div[2]')
        min_img.screenshot('./min_img.png') # 小图片

        max_img = self.basechrom.find_element('/html/body/div[4]/div[2]/div[6]/div/div/div[2]/div[1]/div/div[2]')
        max_img.screenshot('./max_img.png') # 大图片


if __name__ == '__main__':

    b = Bilibili()
    b.home()
    b.show_login_window()
    b.username_passwor_login('18986680202','Abc123456')

