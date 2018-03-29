# -*- coding: utf-8 -*-
from base.base_driver import get_driver


class GetDriver():
    @classmethod
    def getdriver(cls):
        cls.driver = get_driver("com.android.settings", ".Settings")
        return cls.driver

    def closedriver(self):
        self.driver.quit()
