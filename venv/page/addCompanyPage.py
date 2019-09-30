from page.basePage import  BasePage
from selenium.webdriver.common.by import By

class AddCompanyPage(BasePage):
    #左侧基础信息管理
    jichu_loc = (By.CSS_SELECTOR, "li.ant-menu-submenu:nth-child(2) > div:nth-child(1) > span:nth-child(1) > span:nth-child(2)")

    #左侧分公司管理
    brarchComp_loc = (By.CSS_SELECTOR, "#\/basicinfo\$Menu > li:nth-child(1) > a:nth-child(1)")

    #新增按钮
    addComy_loc = (By.CSS_SELECTOR, ".ant-btn-background-ghost")

    #新增-分公司名称
    comyName_loc = (By.CSS_SELECTOR, "div.modelStyle___YmdHO:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > input:nth-child(1)")

    #分公司简称
    simpleComyName_loc = (By.CSS_SELECTOR, "div.modelStyle___YmdHO:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > input:nth-child(1)")

    #所属分公司
    belowCompany_loc = (By.CSS_SELECTOR, "div.modelStyle___YmdHO:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1)")

    #分公司联系人
    contactName_loc = (By.ID, "contactName")

    #分公司联系电话
    contactPhone_loc = (By.ID, "contactPhone")

    #共享总公司账户 是
    shareyes_loc = (By.CSS_SELECTOR, "label.ant-radio-wrapper:nth-child(2) > span:nth-child(1)")

    #共享总公司账户 否
    shareno_loc = (By.CSS_SELECTOR, ".ant-radio-checked")

    #可添加备注说明
    remark_loc = (By.ID, "remark")

    #确定
    sure_loc = (By.CSS_SELECTOR, "button.ant-btn-primary:nth-child(2)")

    #所属分公司的下拉框
    shuyu_la = (By.CSS_SELECTOR, "div.modelStyle___YmdHO:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2) > i:nth-child(1) > svg:nth-child(1)")
    one = (By.CSS_SELECTOR, "li.ant-select-dropdown-menu-item:nth-child(1)")

    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self):
        self._open(self.url, self.pagetitle)

    #点击基础信息管理
    def open_jichu(self):
        self.click_element(*self.jichu_loc)

    #点击分公司管理
    def open_fenCompany(self):
        self.click_element(*self.brarchComp_loc)

    # 添加添加
    def click_add(self):
        self.click_element(*self.addComy_loc)

    #分公司名称
    def sendK_fenCompanyName(self, companyName):
        self.send_keys(companyName, *self.comyName_loc)

    #分公司简称
    def sendK_fenSimCompanyName(self, simpleComyName):
        self.send_keys(simpleComyName, *self.simpleComyName_loc)

    #所属分公司
    def select_shuyu(self):
        self.click_element(*self.shuyu_la)
        self.click_element(*self.one)

    #联系人
    def sendK_telePeople(self, contactName):
        self.send_keys(contactName, *self.contactName_loc)

    #联系电话
    def sendK_telePhone(self, contactPhone):
        self.send_keys(contactPhone, *self.contactPhone_loc)

    #允许共享分公司账户
    def click_allow(self):
        self.click_element(*self.shareyes_loc)

    #禁止共享分公司账户
    def click_forbid(self):
        self.click_element(*self.shareno_loc)

    #备注
    def sendK_remark(self,remark):
        self.send_keys(remark, *self.remark_loc)

    #确定
    def click_confirm(self):
        self.click_element(*self.sure_loc)




