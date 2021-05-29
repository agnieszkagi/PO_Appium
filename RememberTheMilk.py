import unittest
import os

from appium import webdriver
from locators import GeneralLocators
from locators import RegisterPageLocators
from locators import LoginPageLocators
from locators import HomePageLocators


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestRememberTheMilk(unittest.TestCase):
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

    '''
    def test1RegistrationWithWronEmail(self):
        self.driver.is_app_installed(GeneralLocators.REMEMBER_THE_MILK_APP)
        #click skip button if displayed
        list = self.driver.find_elements_by_id(GeneralLocators.SKIPP_BUTTON)
        if len(list)>0:
            list[0].click()

        #click sign in button
        el = self.driver.find_element_by_id(RegisterPageLocators.SING_IN_BUTTON)
        el.click()
        #Data input
        el = self.driver.find_element_by_id(RegisterPageLocators.NAME_INPUT)
        el.send_keys("Agnieszka")
        el= self.driver.find_element_by_id(RegisterPageLocators.SURNAME_INPUT)
        el.send_keys("Nowak")
        el = self.driver.find_element_by_id(RegisterPageLocators.EMAIL_INPUT)
        el.send_keys("anowak.com")
        el = self.driver.find_element_by_id(RegisterPageLocators.USERNAME_INPUT)
        el.send_keys("testernowak")
        el = self.driver.find_element_by_id(RegisterPageLocators.PASSWORD_INPUT)
        el.send_keys("passswwwo")
        el = self.driver.find_element_by_class_name(RegisterPageLocators.SIGN_IN)
        el.click()

        # Assertions
        el = self.driver.find_element_by_id(RegisterPageLocators.ALERT_WINDOW)
        assert el.is_displayed() == True
        el = self.driver.find_element_by_id(RegisterPageLocators.INVALID_EMAIL_MESSAGE)
        assert el.text == 'Email invalid.'

    
    def test2SuccesfulLogin(self):
        self.driver.is_app_installed(GeneralLocators.REMEMBER_THE_MILK_APP)
        # click skip button if displayed
        list = self.driver.find_elements_by_id(GeneralLocators.SKIPP_BUTTON)
        if len(list) > 0:
            list[0].click()
        # click log in button
        el = self.driver.find_element_by_id(LoginPageLocators.LOGIN_BUTTON)
        el.click()
        # username and password input
        el = self.driver.find_element_by_id(LoginPageLocators.USERNAME_FIELD)
        el.send_keys('testeraga')
        el = self.driver.find_element_by_id(LoginPageLocators.PASSWORD_FIELD)
        el.send_keys('Tester1234!')
        el = self.driver.find_element_by_xpath(LoginPageLocators.LOG_IN)
        el.click()

        #Assertion
        el = self.driver.find_element_by_xpath(LoginPageLocators.HOME_TAB)
        assert el.is_displayed() == True
    '''

    def test3AddTask(self):
        self.driver.is_app_installed(GeneralLocators.REMEMBER_THE_MILK_APP)
        # click skip button if displayed
        list = self.driver.find_elements_by_id(GeneralLocators.SKIPP_BUTTON)
        if len(list) > 0:
            list[0].click()
        el = self.driver.find_element_by_id(LoginPageLocators.LOGIN_BUTTON)
        el.click()
        el = self.driver.find_element_by_id(LoginPageLocators.USERNAME_FIELD)
        el.send_keys('testeraga')
        el = self.driver.find_element_by_id(LoginPageLocators.PASSWORD_FIELD)
        el.send_keys('Tester1234!')
        el = self.driver.find_element_by_xpath(LoginPageLocators.LOG_IN)
        el.click()
        el = self.driver.find_element_by_xpath(HomePageLocators.STUDIA_TAB)
        el.click()



if __name__ == 'main':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRememberTheMilk)
    unittest.TextTestRunner(verbosity=2).run(suite)
