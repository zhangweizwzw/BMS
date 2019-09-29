from testCase.baseCase import BaseCase
from page.loginPage import LoginPage
from common.commonVar import CommonVar
import unittest
from time import sleep
from common.getXlsxData import ExcelUtil

'''
    登录用例
    @auther zw
    2019-4-29
'''
class Login(BaseCase):


    #读取excel数据
    #循环执行用例
    def getData(self):
        filePath = r"../data/userinfo.xlsx"
        sheetName = "Sheet1"
        data=ExcelUtil(filePath,sheetName).dict_data()
        return data

    #执行登录操作
    def doLogin(self,loginPage,data):
        loginPage.input_userName(data.get("userName"))
        loginPage.input_passWord(data.get("passWord"))
        loginPage.input_imageCode(data.get("imageCode"))
        loginPage.login()

        message=data.get("message")
        if message == "success":
            if loginPage.isLoginSuccess():
                sleep(2)
                loginPage.logout()
            else:
                self.assertEqual("登录失败",message, "登录成功用例执行失败")
        else:
            errorlog = loginPage.error_log()
            sleep(2)
            # print(errorlog)
            self.assertEqual(errorlog, message, " %s case执行错误" % message)

        sleep(4)

    #主方法
    def test_Login(self):
        # 获取excel数据
        data = self.getData()
        loginPage = LoginPage(self.driver, self.url, u"login")
        loginPage.open()
        for i in data:
            self.doLogin(loginPage,i)


if __name__ == "__main__":
    unittest.main()



'''单个执行用例
    #登陆成功
    def test_Login(self):
        loginPage=LoginPage(self.driver,self.url,u"user/login")

        loginPage.open()
        loginPage.input_userName(CommonVar.URERNAME)
        loginPage.input_passWord(CommonVar.PASSWORD)
        loginPage.input_imageCode(CommonVar.IMAGECODE)
        loginPage.login()
        sleep(4)
        loginPage.logout()

    def test_LoginErr(self):
        loginPage = LoginPage(self.driver, self.url, u"user/login")

        loginPage.open()
        loginPage.input_userName("nihaoa")
        loginPage.input_passWord(CommonVar.PASSWORD)
        loginPage.input_imageCode(CommonVar.IMAGECODE)
        loginPage.login()
        errorlog=loginPage.error_log()
        print(errorlog)
        sleep(4)
        self.assertEqual(errorlog,"用户不存在","用户不存在case执行错误")
    '''
        