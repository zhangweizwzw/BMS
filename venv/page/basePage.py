from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
'''
    所有page页面父类
    @auther zw
    2019-4-29
'''
class BasePage(object):

    def __init__(self, driver,url,pagetitle):
        self.driver=driver
        self.url=url
        self.pagetitle=pagetitle

    #根据页面title判断进入页面是否正确
    def onPage(self,pageTitle):
        return pageTitle in self.driver.current_url

    #定义私有方法，
    def _open(self,url,pagetitle):
        self.driver.get(url)
        self.driver.maximize_window()


    #调用_open方法，打开浏览器
    def open(self):
        self._open(self.url,self.pagetitle)

    def isElementExists(self,*loc):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(loc))
            # return self.driver.find_element(*loc)
            return True
        except:
            print(u" %s 页面中未能找到 %s 元素" % (self, loc))
            return False

    #重写定义查找元素
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print(u" %s 页面中未能找到 %s 元素" % (self, loc))

    # 重写定义send_keys方法
    def send_keys(self,vaule, *loc, clear_first=True):
        try:
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
            else:
                self.find_element(*loc).clear()

        except AttributeError:
            print(u" %s 页面中未能找到 %s 元素" % (self, loc))

    #重写定义点击元素
    def click_element(self,*loc):
        try:
            self.find_element(*loc).click()
        except:
            print(u" %s 页面中未能找到 %s 元素" % (self, loc))


    #重写定义获取text
    def get_text(self,*loc):
        try:
            return self.find_element(*loc).text
        except:
            print(u" %s 页面中未能找到 %s 元素" % (self, loc))