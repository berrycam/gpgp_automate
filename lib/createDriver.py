# -*- coding: utf-8 -*-
'''
Created on 2018.10.19

@author: chenaimei
'''
import os
import re
from appium import webdriver

def get_deviceInfo():
    # 读取设备 id，记得设备要开启，否则会在此处报错，可优化
    readDeviceId = list(os.popen('adb devices').readlines())
    # 正则表达式匹配出 id 信息
    deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
    # 读取设备系统版本号
    deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
    deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]
    return deviceId, deviceVersion


def get_driver():
    """
    :创建desired_caps
    """
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = get_deviceInfo()[1]
    desired_caps['deviceName'] = get_deviceInfo()[0]
    desired_caps['unicodeKeyboard'] = 'True'  #设置键盘隐藏
    desired_caps['resetKeyboard'] = 'True'    #恢复键盘设置
    desired_caps['autonationName'] = 'Uiautomator2'
    desired_caps['appPackage'] = 'com.konsung.familydoctor'
    desired_caps['appActivity'] = '.ui.LoginActivity'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    
    return driver