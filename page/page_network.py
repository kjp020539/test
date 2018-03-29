# -*- coding: utf-8 -*-
import os, sys

from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())
from base.base_action import BaseAction
from page.test_package import GetDriver


class NetWork(BaseAction):
    def __init__(self):
        BaseAction.__init__(self, GetDriver.getdriver())
        self.seach_loc = By.ID, "com.android.settings:id/search"
        self.more = By.XPATH, ("text", "更多")
        self.network = By.XPATH, ("text", "移动网络")
        self.network_type = By.XPATH, ("text", "首选网络类型")
        self.network_2G = By.XPATH, ("text", "2G")

    def click_search(self):
        self.find_element(self.seach_loc).click()

    def click_more(self):
        self.find_element(self.more).click()

    def click_network(self):
        self.find_element(self.network).click()

    def click_networktype(self):
        self.find_element(self.network_type).click()

    def click_2G(self):
        self.find_element(self.network_2G).click()
