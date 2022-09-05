from re import T
from trace import Trace
import scrapy
import re

class Demo1Spider(scrapy.Spider):
    name = 'demo1'
    allowed_domains = ['mail.163.com']
    start_urls = ['https://mail.163.com/js6/main.jsp?sid=HBwTcoKhFDXkPCBguihhmFsBmtpRVbWT&df=mail163_letter#module=welcome.WelcomeModule%7C%7B%7D']

    def start_requests(self):
        cookies = "_ntes_nnid=1e45edcce56206c81144b659c3b3f206,1660732473857; _ntes_nuid=1e45edcce56206c81144b659c3b3f206; NTES_P_UTID=qkEQJ39n8uWEoYN9VNRq7EFxamrcy9A2|1662111527; NTES_SESS=SHoneuxvM73uXwCfW57DDToABAenjiv2lo4toDXs7mDmv4jcvh2dqAD6G1HxOvDhcx2SxCFFsrOWRnFdVQtfIu1ykyvrum534e7JKF_0fYc5Ybsc.7TyLT0.se_BYAjiVaH_3sOqGEViBK2HMShc8LNPbykGV79cFkXGBaEDkQUzDuezCMvRGLFozy6bMwrLuV7_wORFAXbFWJX37LSyzAt7NIkd.YXQt; NTES_PASSPORT=Hszf3JHItrnAuS3N_21RgmmZ_wYitSpddUT_AW1PisFb.6Js.4TFkUnoMuqiX.n4sogkpwy3K0vUS1wEd81Yh8vp6Em8Fd39gqRHcVwoHOLcHvyRh2D0pYS3QA4rcDMM7X5jJxlI7dGuGDivQEb6buIw4vqhAsG0y22xL0z8X2FIXLHy5NAx4A.1eKUOsrOaz; S_INFO=1662111527|0|3&80##|m18986680202_1; P_INFO=m18986680202_1@163.com|1662111527|1.json|mail163|00&99|hub&1661871524&youdaodict_client#hub&420900#10#0#0|189202&1.json|youdaodict_client|18986680202@163.com; mail_upx_nf=; mail_idc=""; MAIL_SDID=883043184178515968; MAIL_SESS=SHoneuxvM73uXwCfW57DDToABAenjiv2lo4toDXs7mDmv4jcvh2dqAD6G1HxOvDhcx2SxCFFsrOWRnFdVQtfIu1ykyvrum534e7JKF_0fYc5Ybsc.7TyLT0.se_BYAjiVaH_3sOqGEViBK2HMShc8LNPbykGV79cFkXGBaEDkQUzDuezCMvRGLFozy6bMwrLuV7_wORFAXbFWJX37LSyzAt7NIkd.YXQt; MAIL_SINFO=1662111527|0|3&80##|m18986680202_1; MAIL_PINFO=m18986680202_1@163.com|1662111527|1.json|mail163|00&99|hub&1661871524&youdaodict_client#hub&420900#10#0#0|189202&1.json|youdaodict_client|18986680202@163.com; MAIL_PASSPORT_INFO=m18986680202_1@163.com|1662111527|1.json; secu_info=1.json; locale=; face=js6; mail_style=js6; mail_uid=m18986680202_1@163.com; mail_host=mail.163.com; stats_session_id=4c6d80b6-8f7c-482e-a307-5f4173d90a44; starttime=; Coremail=cb4794b38d501%HBwTcoKhFDXkPCBguihhmFsBmtpRVbWT%g6a56.mail.163.com; MAIL_ENTRY_INFO=1.json|0|mail163|mail163_letter|117.152.93.117||; MAIL_ENTRY_CS=c7777075373f0357348d05f43ae86ad0; cm_last_info=dT1tMTg5ODY2ODAyMDJfMSU0MDE2My5jb20mZD1odHRwcyUzQSUyRiUyRm1haWwuMTYzLmNvbSUyRmpzNiUyRm1haW4uanNwJTNGc2lkJTNESEJ3VGNvS2hGRFhrUENCZ3VpaGhtRnNCbXRwUlZiV1Qmcz1IQndUY29LaEZEWGtQQ0JndWloaG1Gc0JtdHBSVmJXVCZoPWh0dHBzJTNBJTJGJTJGbWFpbC4xNjMuY29tJTJGanM2JTJGbWFpbi5qc3AlM0ZzaWQlM0RIQndUY29LaEZEWGtQQ0JndWloaG1Gc0JtdHBSVmJXVCZ3PWh0dHBzJTNBJTJGJTJGbWFpbC4xNjMuY29tJmw9LTEmdD0tMSZhcz10cnVl; Coremail.sid=HBwTcoKhFDXkPCBguihhmFsBmtpRVbWT; mail_upx=c3bj.mail.163.com|c4bj.mail.163.com|c5bj.mail.163.com|c6bj.mail.163.com|c7bj.mail.163.com|c7bj.mail.163.com|c3bj.mail.163.com|c4bj.mail.163.com|c5bj.mail.163.com|c6bj.mail.163.com; MAIL_PASSPORT=GfCt2aRtRlnWV4WS6pxzNKdAZvWZ0kWoVfJt8geY6U5wrOhUrIJ5LfvXnHM6srvIUXTLq02._oCfpe0bl1ezN1CqObx15l.BTMiGAa0XGc3AGC2iNjWoqzp.78IRAWnndsyEh4kVdlDHDW6C7bwOwHV0ICMN8UDo2jj43oK1sj5Vs3G2yP84I8reZ_fcURc9K; mail_entry_sess=10c9bad8ee9fa4a781dda6d6a3d5159faaf296fadd4549786dd0f7ad4a3f7fddfe87d3ab43583f190423e9d94028012e455f91c143c6d75b7537e8a968bfaf7b0b9c3f3d8b918d18e369bad58ce6d71246ff4ef56b5081770d138c6c2630be6c539f7897f49d44d9e64bd6729aa270c069112fc714dbfa8aaf513eaab4d1cdbd3a3637e2c1cd6972ef1b13b22d9a636af84b5df39e6b143c53e146e81662465cb6f02f86f6171bb6fc35c7f9fb2670f2281d3e463bc0565e37402146d1f1bed3; JSESSIONID=947503C047EA5C31E2649862B2D31855"
        cookies = { i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
        yield scrapy.Request(
            self.start_urls[0],
            callback = self.parse,
            cookies = cookies
        )
    
    def parse(self, response):
        # print(response.xpath('//*[@id="spnUid"]/text()').get())
        # print(response.text)
        print(re.findall(r"'true_name':'(\d+)'",response.text))
     