from page.basePage import BasePage
from selenium.webdriver.common.by import By
from common.commonfun import CommonFun

class AddDrvierPage(BasePage):
    # 左侧基础信息管理
    jichu_loc = (By.CSS_SELECTOR, "li.ant-menu-submenu:nth-child(2) > div:nth-child(1) > span:nth-child(1) > span:nth-child(2)")

    #左侧司机管理
    driverManage_loc= (By.CSS_SELECTOR, "li.ant-menu-item:nth-child(2) > a:nth-child(1)")

    #新增按钮
    addDriver_loc=(By.CSS_SELECTOR, "button.ant-btn-background-ghost:nth-child(1)")

    #司机手机号
    employeeMobile_loc= (By.CSS_SELECTOR, "div.modelStyle___YmdHO:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > input:nth-child(1)")

    #司机姓名
    employeeName_loc= (By.CSS_SELECTOR, "div.modelStyle___YmdHO:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > input:nth-child(1)")


    #所属分公司下拉
    shuComp_loc= (By.CSS_SELECTOR, "div.modelStyle___YmdHO:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2) > i:nth-child(1) > svg:nth-child(1)")
    #选择第一个
    dian_click_loc=(By.CSS_SELECTOR, "div.modelStyle___YmdHO:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)")

    #备注
    remark_loc= (By.ID, "remark")

    #确定按钮
    sure_loc= (By.CSS_SELECTOR, ".ant-modal-footer > div:nth-child(1) > button:nth-child(2)")

    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self):
        self._open(self.url, self.pagetitle)

    #点击左侧司机管理
    def click_jichuMan(self):
        self.click_element(*self.jichu_loc)

    #点击新增按钮
    def click_add(self):
        self.click_element(*self.addDriver_loc)

    #点击左侧司机管理
    def click_driverMan(self):
        self.click_element(*self.driverManage_loc)

    #输入司机手机号
    def sendK_employeeMobile(self,eMobile):
        self.send_keys(eMobile, *self.employeeMobile_loc)

    #输入司机姓名
    def sendK_employeeName(self,employeeName):
        self.send_keys(employeeName, *self.employeeName_loc)

    #选择所属分公司
    def sele_Company(self):
        self.click_element(*self.shuComp_loc)
        self.click_element(*self.dian_click_loc)

    #添加备注
    def sendk_remark(self,remark):
        self.send_keys(remark, *self.remark_loc)

    #点击确定
    def click_sure(self):
        self.click_element(*self.sure_loc)



