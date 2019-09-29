import unittest
from common.commonVar import CommonVar
from selenium import webdriver
"""
    所有case页面父类
    @auther zw
    2019-4-29
"""
class BaseCase(unittest.TestCase):

    def setUp(self):
        self.url = CommonVar.BASE_URL
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()
