
import scrapy


class Demo01Spider(scrapy.Spider):
    name = 'github01'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        authenticity_token = response.xpath('//*[@id="login"]/div[4]/form/input[1.json]/@value').extract_first()
        timestamp_secret = response.xpath('//*[@id="login"]/div[4]/form/div/input[11]/@value').extract_first()
        timestamp = response.xpath('//*[@id="login"]/div[4]/form/div/input[10]/@value').extract_first()
        post_data = {
            'commit' : 'Sign in',
            'authenticity_token' : authenticity_token,
            'login' : '815931614@qq.com',
            'password' : 'qwe7410852963.',
            'trusted_device' : '',
            'webauthn-support' : 'supported',
            'webauthn-iuvpaa-support' : 'unsupported',
            'return_to' : 'https://github.com/login',
            'allow_signup' : '',
            'client_id' : '',
            'integration' : '',
            'required_field_4210' : '',
            'timestamp' : timestamp,
            'timestamp_secret' : timestamp_secret,
        }
        yield scrapy.FormRequest(
            'https://github.com/session',
            formdata=post_data,
            callback=self.after_login
        )


    def after_login(self,response):
        import re
        print(re.findall('815931614',response.text))