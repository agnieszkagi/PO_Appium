import unittest
import os

from appium import webdriver
from time import sleep

from click._unicodefun import click

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Test1Appium(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['app'] = PATH('contactmanager.apk')
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Genymotion Cloud' #jsli faktyczny tel to nazwa telefonu
        desired_caps['udid'] = 'localhost:10000'  # do uzupelnia gdyby nie byl staly; wynik adb devices
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'

        # polaczenie z Appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.quit()

    def testForm(self):
        self.driver.is_app_installed('com.example.android.contactmanager')
        self.driver.find_element_by_id('com.example.android.contactmanager:id/addContactButton').click()
        textfields = self.driver.find_elements_by_class_name('android.widget.EditText')
        textfields[0].send_keys('Malwina z Wroclawia')
        textfields[1].send_keys('555444333')
        textfields[2].send_keys('malwina@wsb.pl')
        sleep(2)

        # printy dydaktycznie
        print(textfields[0])
        print(textfields[0].text)

        # asercja
        self.assertEqual('Malwina z Wroclawia', textfields[0].text)
        self.assertEqual('555444333', textfields[1].text)
        self.assertEqual('malwina@wsb.pl', textfields[2].text)


        '''
        self.driver.find_element_by_id('com.example.android.contactmanager:id/contactNameEditText').send_keys('AgaG')
        self.driver.find_element_by_id('com.example.android.contactmanager:id/contactPhoneEditText').send_keys('666555444')
        self.driver.find_element_by_id('ccom.example.android.contactmanager:id/contactEmailEditText').send_keys('agag@cc')

        el = self.driver.find_elements_by_id('com.android.permissioncontroller:id/continue_button')
        click(el)

        el = self.driver.find_elements_by_id('com.example.android.contactmanager:id/contactNameEditText')
        if el.isDisplayed():
            print('Text field found')
            el.sendKeys('Aga')
        '''


if __name__ == 'main':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test1Appium)
    unittest.TextTestRunner(verbosity=2).run(suite)