'''
Created Date: Wednesday August 18th 2021 7:09:11 pm
Author: Andrés X. Vargas
-----
Last Modified: Thursday August 19th 2021 12:52:18 am
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''
from unittest import TestCase, main
from HtmlTestRunner import HTMLTestRunner
from appium import webdriver
from time import sleep


class AcceptanceTestCancelOrder(TestCase):

    @classmethod
    def setUpClass(cls):
        driver_config = {
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "HWJKM-H",
            "automationName": "UiAutomator2",
            "appPackage": "com.mattu.restaurant",
            "appActivity": ".MainActivity"
        }
        cls.driver = webdriver.Remote(
            'http://127.0.0.1:4723/wd/hub', driver_config)
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_a_menu_list_renders_correctly(self):
        driver = self.driver
        button = driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup')
        button.click()
        sleep(5)
        menu_plates = driver.find_elements_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[1]')
        self.assertGreater(len(menu_plates), 0)

    def test_b_click_on_plate(self):
        driver = self.driver
        plate = driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]')
        plate.click()
        sleep(5)
        title = driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView').text
        self.assertEqual(title, 'Panqueques')

    def test_c_order_plate_modal_appear(self):
        print("SCROLL DOWN NOW!!")
        sleep(5)
        driver = self.driver
        button = driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView')
        button.click()
        title = driver.find_element_by_id('android:id/alertTitle').text
        self.assertEqual(title, 'Order plate confirmation')

    def test_d_confirm_plate(self):
        driver = self.driver
        confirm_button = driver.find_element_by_id('android:id/button2')
        confirm_button.click()
        title = driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.View').text
        self.assertEqual(title, 'Summary of the order')

    def test_e_confirm_order_modal_appear(self):
        driver = self.driver
        confirm_button = driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup')
        confirm_button.click()
        title = driver.find_element_by_id('android:id/alertTitle').text
        self.assertEqual(title, 'Final order confirmation')

    def test_f_confirm_order(self):
        driver = self.driver
        confirm_button = driver.find_element_by_id('android:id/button1')
        confirm_button.click()
        title = driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.View').text
        self.assertEqual(title, 'Summary of the order')

    def test_g_delete_plate(self):
        driver = self.driver
        delete_button = driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup')
        delete_button.click()
        title = driver.find_element_by_id('android:id/alertTitle').text
        self.assertEqual(title, 'Delete plate from order')

    def test_h_confirm_delete_plate(self):
        driver = self.driver
        delete_button = driver.find_element_by_id('android:id/button2')
        delete_button.click()
        title = driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView').text
        self.assertEqual(title, ' Total: $0.00')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    main(verbosity=2, testRunner=HTMLTestRunner(
        output="reports/acceptance_reports/", report_name="test_menu"))
