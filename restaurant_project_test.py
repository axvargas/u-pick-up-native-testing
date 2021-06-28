'''
Created Date: Sunday June 27th 2021 4:23:05 pm
Author: Andrés X. Vargas
-----
Last Modified: Sunday June 27th 2021 6:08:07 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
from unittest import TestCase, main
from HtmlTestRunner import HTMLTestRunner
from appium import webdriver

class NewOrderTest(TestCase):

    @classmethod
    def setUpClass(cls):
        driver_config = {
            "platformName": "Android",
            "platformVersion": "10",
            "deviceName": "HWMAR",
            "automationName": "UiAutomator2",
            "appPackage": "com.mattu.restaurant",
            "appActivity": ".MainActivity"
        }
        cls.driver = webdriver.Remote(
            'http://127.0.0.1:4723/wd/hub', driver_config)
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_renders_correctly(self):
        driver = self.driver
        text = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView').text
        self.assertEqual(text, "New Order")

    def test_transition_to_menu(self):
        driver = self.driver
        button = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup')
        button.click()

        menu_text = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.View').text
        self.assertEqual(menu_text, "Menu")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    main(verbosity=2, testRunner=HTMLTestRunner(
        output="reports/report_restaurant", report_name="test_restaurant"))
