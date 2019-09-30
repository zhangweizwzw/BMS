import unittest
from testCase.login import Login
from testCase.addCompany import AddCompany
from testCase.addDrvier import AddDrvier
from common.HTMLTestRunner import HTMLTestRunner
import time
from common.sendEmail import SendEmail

'''
    TestSuite 用例执行
    @auther zw
    2019-4-30
'''
# suite.addTest(Login("test_Login"))
# suite.addTest(AddCompany("test_addCompany"))

if __name__=="__main__":
    suite = unittest.TestSuite()
    suite.addTest(AddDrvier("test_addDriver"))


'''
    #保存执行结果到report目录
    report_name=time.strftime("%Y-%m-%d %H__%M__%S", time.localtime())+"_result.html"
    reportAddress="../report/"+report_name;
    fileReport=open(reportAddress,"wb")
    runner=HTMLTestRunner(stream=fileReport, title='BMS企业后台测试报告', description='用例执行情况：')
    runner.run(suite)
    fileReport.close()
    #发送测试报告邮件
    SendEmail.send_email(reportAddress)
'''