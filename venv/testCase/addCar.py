from testCase.baseCase import BaseCase
import unittest
from page.loginPage import LoginPage
from page.addCarPage import AddCarPage
from common.commonVar import CommonVar
import random
from time import sleep

class AddCar(BaseCase):

    def goLogin(self):
        loginPage = LoginPage(self.driver, self.url, u"login")
        loginPage.open()
        loginPage.input_userName(CommonVar.USERNAME)
        loginPage.input_passWord(CommonVar.PASSWORD)
        loginPage.input_imageCode(CommonVar.IMAGECODE)
        loginPage.login()

    def addCar(self):
        addCarPage = AddCarPage(self.driver, self.url, u'vehicle')
        addCarPage.click_jichuMan()
        addCarPage.click_carMan()
        addCarPage.click_addCar()
        addCarPage.sele_diqu()
        addCarPage.sele_xuhao()
        addCarPage.sendK_carNo(random.randint(10000, 99999))
        addCarPage.sele_carType()
        addCarPage.click_sure()


    def test_addCar(self):
        self.goLogin()
        self.addCar()

if __name__ == "__main__":
    unittest.main()