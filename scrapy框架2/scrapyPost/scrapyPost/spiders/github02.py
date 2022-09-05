from calendar import c
import scrapy


class Github02Spider(scrapy.Spider):
    name = 'github02'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']



    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response, # 自动重response中寻找from表单
            formdata={
                'login' : '815931614@qq.com',
                'password' : 'qwe7410852963.',
            },
            callback= self.after_login
        )
    def after_login(self,response):
        import re
        print(re.findall('815931614',response.text))