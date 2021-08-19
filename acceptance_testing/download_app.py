'''
Created Date: Wednesday August 18th 2021 3:28:38 am
Author: Andrés X. Vargas
-----
Last Modified: Wednesday August 18th 2021 3:34:12 am
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
from unittest import TestCase, main
from HtmlTestRunner import HTMLTestRunner
from appium import webdriver
from time import sleep


class Assertions(TestCase):

    @classmethod
    def setUpClass(cls):
        driver_config = {
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "HWJKM-H",
            "automationName": "UiAutomator2",
            "appPackage": "com.android.vending",
            "appActivity": ".AssetBrowserActivity"
        }
        cls.driver = webdriver.Remote(
            'http://127.0.0.1:4723/wd/hub', driver_config)

    def test_download_app(self):
        driver = self.driver
        driver.implicitly_wait(10)
        sleep(5)

        driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView').click()
        sleep(2)

        driver.hide_keyboard()

        sleep(2)

        text_field = driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.EditText')
        text_field.send_keys('mattu restaurant')
        sleep(2)

        # * press enter
        driver.press_keycode(66)
        sleep(2)
        driver.hide_keyboard()

        driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.ViewGroup').click()
        sleep(2)

        driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button').click()
        sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    main(verbosity=2, testRunner=HTMLTestRunner(
        output="reports/report_test", report_name="test_to_play"))
