# -*- coding: utf-8 -*-
import os, sys

from page.page_network import NetWork

sys.path.append(os.getcwd())


class TestNetWork():

    def setup_class(self):
        self.page_network = NetWork()

    def test_network_2G(self):
        self.page_network.click_more()
        self.page_network.click_network()
        self.page_network.click_networktype()
        self.page_network.click_2G()

    def teardown_class(self):
        self.page_network.driver.quit()
