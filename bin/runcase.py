# -*- coding: utf-8 -*-
'''
Created on 2018.10.24

@author: chenaimei
'''
import unittest

# 可优化，配置化
test_path = r'../testcase/'

if __name__ == '__main__':
    """
    :查找测试目录并执行
    """
    discover = unittest.defaultTestLoader.discover(test_path, pattern='test_*.py')
    unittest.TextTestRunner(verbosity=2).run(discover)