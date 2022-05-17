# !/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：ApiAutoTest 
@File ：test_Login.py
@Author ：琴师
@Date ：2022/5/4 4:01 下午 
'''
import os,json,allure
from utils.RequestsUtil import RequestLogic
from utils.YamlUtil import YamlReader
from utils.AssertUtil import Assert
from utils.LogUtil import my_log
from config.Conf import ConfigYaml
from common.ExcelData import CaseData
from common import ExcelConfig
from config import Conf
from common import Base
import pytest


test_file = os.path.join(Conf.get_caselist_path(),"test_Login.yml")
cast_list = YamlReader(test_file).reader_all()

class Test(object):

    def setup_class(self):

        self.Log = my_log(log_name=os.path.basename(__file__))
        self.request = RequestLogic()

    @pytest.mark.parametrize("login",cast_list)
    def test_login(self,login):
        """
        Case--密码登录(phone正常,pwd正常)
        """
        url = ConfigYaml().get_conf_UmsTestUrl() + login.get("Url")
        data = login.get("data")
        print(type(data))
        self.Log.info("request data：%s" % (str(data)))
        headers = login.get("headers")
        response_json = self.request.request_post(url=url,data=data)
        self.Log.info("response data：%s" % (str(response_json)))

    def test_gettoken(self,get_loginToken):
        a = get_loginToken
        print("我已经正常获取到token啦",a)


    def teardowm_class(self):
        pass


if __name__=="__main__":
    report_path = Conf.get_report_path() + os.sep + "result"
    report_html_path = Conf.get_report_path() + os.sep + "html"
    pytest.main(["-s", "test_Login11.py", "--alluredir", report_path])
    Base.allure_report(report_path, report_html_path)
    Base.send_email(title="接口测试报告", content=report_html_path)


