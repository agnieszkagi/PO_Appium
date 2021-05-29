import unittest
import os

from appium import webdriver
from time import sleep
from locators import RegisterPageLocators

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Test2Appium(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['app'] = PATH('RememberTheMilk.apk')
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Genymotion Cloud'
        desired_caps['udid'] = 'localhost:10000'
        desired_caps['appPackage'] = 'com.rememberthemilk.MobileRTM'
        desired_caps['appActivity'] = 'com.rememberthemilk.MobileRTM.Activities.RTMWelcomeActivity'
        desired_caps['noReset'] = 'true' #zeby zapisywalo zmiany

        # polaczenie z Appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.quit()

    def testRegistrationWithWronEmail(self):
        self.driver.is_app_installed('com.rememberthemilk.MobileRTM')
        #click skip button if displayed
        list = self.driver.find_elements_by_id('com.rememberthemilk.MobileRTM:id/alert_generic_notice')
        if len(list)>0:
            list[0].click()
        #if self.driver.find_element_by_id('com.rememberthemilk.MobileRTM:id/alert_generic_notice'):
        #    self.driver.find_element_by_id('com.rememberthemilk.MobileRTM:id/alert_generic_notice').click()

        #click register button
        #self.driver.find_element_by_id('com.rememberthemilk.MobileRTM:id/sign_button').click()
        el = self.driver.find_element_by_id(RegisterPageLocators.SING_IN_BUTTON)
        el.click()
        #Data input
        self.driver.find_element_by_id('com.rememberthemilk.MobileRTM:id/firstname_field').send_keys("Agnieszka")
        self.driver.find_element_by_id('com.rememberthemilk.MobileRTM:id/lastname_field').send_keys("Nowak")
        self.driver.find_element_by_id('com.rememberthemilk.MobileRTM:id/email_field').send_keys("anowak.com")
        self.driver.find_element_by_id('com.rememberthemilk.MobileRTM:id/username_field').send_keys("testernowak")
        self.driver.find_element_by_id('com.rememberthemilk.MobileRTM:id/password_field').send_keys("passswwwo")
        self.driver.find_element_by_class_name('android.widget.Button').click()
        sleep(2)

        # Assertion
        #alert displays
        assert self.driver.find_element_by_id('android:id/alertTitle').is_displayed() == True
        #'email invalid' message displays
        assert self.driver.find_element_by_id('android:id/message').text == 'Email invalid.'

    def testSuccesfulLogin(self):
        self.driver.is_app_installed('com.rememberthemilk.MobileRTM')
        # click skip button if displayed
        list = self.driver.find_elements_by_id('com.rememberthemilk.MobileRTM:id/alert_generic_notice')
        if len(list)>0:
            list[0].click()
        # click log in button
        self.driver.find_element_by_id('com.rememberthemilk.MobileRTM:id/login_button').click()
        self.driver.find_element_by_id('com.rememberthemilk.MobileRTM:id/username_field').send_keys('testeraga')
        self.driver.find_element_by_id('com.rememberthemilk.MobileRTM:id/password_field').send_keys('Tester1234!')
        self.driver.find_element_by_xpath('//*[@text="LOG IN"]').click()
        sleep(1)

        #Assertion
        # home page displays
        assert self.driver.find_element_by_xpath('//*[@text="HOME"]').is_displayed() == True

        sleep(5)

if __name__ == 'main':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test2Appium)
    unittest.TextTestRunner(verbosity=2).run(suite)
