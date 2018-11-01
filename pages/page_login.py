# -*- coding: utf-8 -*-
'''
Created on 2018.10.19

@author: chenaimei
'''
import os
import time
from lib.createDriver import get_driver
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from symbol import except_clause
from selenium.common.exceptions import NoSuchElementException


class LoginPage():
    """
    :登录界面
    """
    def __init__(self):
        """初始化
         TODO:可实现配置化，放置ini
        """
        self._driver = get_driver()
        self._screenshot_path = r'../screenshot/'   # 截图地址
        
        
    def find_toast(self, msg):
        """
        :判断toast消息
        """
        try:
            # timeout = 10, poll_frequency = 0.1
            toast_loc = (By.XPATH, ".//*[contains(@text,'%s')]"%msg)
            element = WebDriverWait(self._driver, 30, 0.05).\
            until(EC.presence_of_all_elements_located(toast_loc))
#             element = WebDriverWait(self._driver, 30, 0.05).\
#             until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, msg)))
            return True
        except:
            return False
        
        
    def login(self, usr, pwd):
        """
        :登录
        """
        self._driver.find_element_by_id('dropview_edit').send_keys(usr)
        self._driver.find_element_by_id('et_password').send_keys(pwd)
        print('  login...', usr)
        self._driver.find_element_by_id("btn_login").click()
        
        # 登录是否成功，最好获取toast信息，家医登录成功时是没有提示的！
        # 换另一种方法，就是找到这个登录成功界面某个ID，如筛选按键，不推荐！仅为示例
        try:
            condition = self._driver.find_element_by_id('btn_condition').text
        except NoSuchElementException as msg:   # 登录失败
            print(u'查找元素异常:%s' % msg)
            now = time.strftime('%Y-%m-%d')
            failed_name = now + r'_' +  usr + u'_用户登录失败.png'
            self._driver.get_screenshot_as_file(self._screenshot_path + failed_name)
            return False
        else:   # 登录成功
            return True
        
        #  TODO：通过toast来判断登录是否成功        
#         if self.find_toast('该用户不存在'):
#             return False
#         elif self.find_toast('账号或密码错误'):
#             return False
#         else:
#             return True

