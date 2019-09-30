from testCase.baseCase import BaseCase
from page.loginPage import LoginPage
from page.addDriverPage import AddDrvierPage
from common.commonfun import CommonFun
from common.commonVar import CommonVar
import random
from time import sleep
import unittest

class AddDrvier(BaseCase):
    def goLogin(self):
        loginPage = LoginPage(self.driver, self.url, u"login")
        loginPage.open()
        loginPage.input_userName(CommonVar.USERNAME)
        loginPage.input_passWord(CommonVar.PASSWORD)
        loginPage.input_imageCode(CommonVar.IMAGECODE)
        loginPage.login()


    def addDriver(self):
        addDriverPage=AddDrvierPage(self.driver, self.url, u'driver')
        addDriverPage.click_jichuMan()
        addDriverPage.click_driverMan()
        sleep(2)
        addDriverPage.click_add()
        addDriverPage.sendK_employeeMobile(CommonFun().getPhone())
        addDriverPage.sendK_employeeName(CommonFun().getName()+"自动化测试")
        addDriverPage.sele_Company()
        addDriverPage.sendk_remark(CommonFun.getChar(random.randint(5, 10)))
        addDriverPage.click_sure()

    def test_addDriver(self):
        self.goLogin()
        self.addDriver()

if __name__=="__main__":
    unittest.main()