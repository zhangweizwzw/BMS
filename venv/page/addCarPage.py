from page.basePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class AddCarPage(BasePage):
    # 左侧基础信息管理
    jichu_loc = (By.CSS_SELECTOR, "li.ant-menu-submenu:nth-child(2) > div:nth-child(1) > span:nth-child(1) > span:nth-child(2)")

    #左侧车辆管理
    carMan_loc = (By.CSS_SELECTOR, "li.ant-menu-item:nth-child(3) > a:nth-child(1)")

    #新增按钮
    add_loc = (By.CSS_SELECTOR, "button.ant-btn-background-ghost:nth-child(1)")

    #地区展开
    diquOpen_loc = (By.CSS_SELECTOR, ".ant-col-7 > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2) > i:nth-child(1) > svg:nth-child(1)")

    #车牌 京
    jing_loc = (By.CSS_SELECTOR, "#\33 cf43b26-2d80-44b2-d82f-47f9696d727f > ul:nth-child(1) > li:nth-child(1)")

    #序号展开
    xuhaoOpen_loc = (By.CSS_SELECTOR, ".ant-col-23 > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2) > i:nth-child(1) > svg:nth-child(1)")


    #序号A
    a_loc = (By.CSS_SELECTOR, "#dd4c8af9-affc-45c9-b3a5-95ab5c8fd6dd > ul:nth-child(1) > li:nth-child(1)")


    #车牌号
    carNum_loc = (By.CSS_SELECTOR, "#number")

    #类型展开
    typeOpen_loc = (By.CSS_SELECTOR, ".ant-col-24 > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2) > i:nth-child(1) > svg:nth-child(1)")

    #类型-自有车
    ziyou_loc = (By.CSS_SELECTOR, "#\37 819c4c5-9fa9-4a80-ec7e-665ffefa436c > ul:nth-child(1) > li:nth-child(1)")

    #确定按钮
    sure_loc = (By.CSS_SELECTOR, ".ant-modal-footer > div:nth-child(1) > button:nth-child(2)")

    #点击基础信息管理
    def click_jichuMan(self):
        self.click_element(*self.jichu_loc)

    #点击车辆管理
    def click_carMan(self):
        self.click_element(*self.carMan_loc)

    #点击新增车辆
    def click_addCar(self):
        self.click_element(*self.add_loc)

    #选择地区
    def sele_diqu(self):
        self.click_element(*self.diquOpen_loc)
        sleep(2)
        self.click_element(*self.jing_loc)

    #选择序号
    def sele_xuhao(self):
        self.click_element(*self.xuhaoOpen_loc)
        self.click_element(*self.a_loc)

    #输入车牌号
    def sendK_carNo(self, carNo):
        self.send_keys(carNo, *self.carNum_loc)

    #选择车辆类型
    def sele_carType(self):
        self.click_element(*self.typeOpen_loc)
        self.click_element(*self.ziyou_loc)

    #点击确定按钮
    def click_sure(self):
        self.click_element(*self.sure_loc)

