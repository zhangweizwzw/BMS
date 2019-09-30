from page.basePage import BasePage
from selenium.webdriver.common.by import By
'''
    登录page页
    @auther zw
    2019-4-29
'''
class LoginPage(BasePage):
    #用户名
    userName_loc = (By.ID, "username")

    #密码
    passWord_loc = (By.ID, "password")

    #图片验证码
    imageCode_loc = (By.CSS_SELECTOR,"input.ant-input:nth-child(1)")

    #登录按钮
    login_loc = (By.CSS_SELECTOR, ".ant-btn")

    #错误提示问题
    err_loc = (By.CSS_SELECTOR, ".ant-message > span:nth-child(1)")

    #姓名选项，退出第一步
    logout_loc = (By.CSS_SELECTOR, ".name___2U6h2")

    #退出按钮
    logout2_loc = (By.CSS_SELECTOR, "li.ant-dropdown-menu-item:nth-child(2)")

    #登录成功油宝，判断登录是否成功
    youbao_loc=(By.CSS_SELECTOR, ".ant-avatar > img:nth-child(1)")

    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self):
        self._open(self.url, self.pagetitle)

    #输入用户名
    def input_userName(self, userName):
        self.send_keys(userName, *self.userName_loc)

    #输入验证码
    def input_passWord(self, passWord):
        self.send_keys(passWord, *self.passWord_loc)

    #输入验证码
    def input_imageCode(self, imageCode):
        self.send_keys(imageCode, *self.imageCode_loc)

    #登录按钮
    def login(self):
        self.click_element(*self.login_loc)

    #退出登录
    def logout(self):
        self.click_element(*self.logout_loc)
        self.click_element(*self.logout2_loc)

    #获取错误信息
    def error_log(self):
        return self.get_text(*self.err_loc)

    #判断是否登录成功
    def isLoginSuccess(self):
        return self.isElementExists(*self.youbao_loc)


