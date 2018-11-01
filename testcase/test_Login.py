# -*- coding: utf-8 -*-
'''
Created on 2018.10.19

@author: chenaimei
'''
import os
import time
import unittest
from ddt import ddt, data, unpack
from lib.common import get_data_cvs
from pages.page_login import LoginPage

# 获取路径
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
    )

# class test
@ddt
class test_Login(unittest.TestCase):
    """
    :家医的登录验证用例
    """
    def setUp(self):
        super(test_Login, self).setUp()

#     def tearDown(self):
#         self.driver.quit()

    @data(*get_data_cvs(
        PATH('../testdata/userlogin.csv')
        ))
    @unpack    
    def test_login_success(self, usr, pwd):
        ret =  LoginPage().login(usr, pwd)
        self.assertEqual(ret, True)
        
 
# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(test_Login)
#     unittest.TextTestRunner(verbosity=2).run(suite)
