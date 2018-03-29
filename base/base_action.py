# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



class BaseAction():

    def __init__(self, driver):
        self.driver = driver

    # 定位单个元素
    def find_element(self, param, timeout=10, poll=1):
        by, value = param
        if by == By.XPATH:
            value = "//*[contains(@" + value[0] + ",'" + value[1] + "')]"
        while True:
            try:
                print(by)
                print(value)
                return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))
            except Exception as e:
                self.driver.swipe(188, 659, 148, 248)

    # 定位多个元素
    def find_elements(self, param, timeout=10, poll=1):
        if param[0] == By.XPATH:
            param[1] = "//*[contains(@" + param[1][0] + ",'" + param[1][1] + "')]"
        while True:
            try:
                return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(param[0], param[1]))
            except Exception as e:
                self.driver.swipe(188, 659, 148, 248)

    # 输入
    def send_keys(self):
        pass
