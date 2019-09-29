from testCase.baseCase import BaseCase
from page.loginPage import LoginPage
from page.addCompanyPage import AddCompanyPage
from time import sleep
from common.commonVar import CommonVar
from common.commonfun import CommonFun
import unittest
import random

class AddCompany(BaseCase):
    def goLogin(self):
        loginPage = LoginPage(self.driver, self.url, u"login")
        loginPage.open()
        loginPage.input_userName(CommonVar.USERNAME)
        loginPage.input_passWord(CommonVar.PASSWORD)
        loginPage.input_imageCode(CommonVar.IMAGECODE)
        loginPage.login()

    #添加公司
    def addcomp(self):
        addCompanyPage = AddCompanyPage(self.driver, self.url, u'subsidiary')
        addCompanyPage.open_jichu()
        addCompanyPage.open_fenCompany()
        addCompanyPage.click_add()
        sleep(2)
        addCompanyPage.sendK_fenCompanyName(CommonFun().getChar(2)+'运输自动化测试')
        addCompanyPage.sendK_fenSimCompanyName(CommonFun().getChar(3))
        addCompanyPage.select_shuyu()
        addCompanyPage.sendK_telePeople(CommonFun().getName())
        addCompanyPage.sendK_telePhone(CommonFun().getPhone())

        aorf=random.random()
        if 0:
            addCompany.click_allow()
        else:
            addCompany.click_forbid()

        addCompany.sendK_remark(CommonFun().getChar(random.randint(5,10)))
        addCompany.click_confirm()


    def test_addCompany(self):
        self.goLogin()
        self.addcomp()



if __name__=="__main__":
    unittest.main()