# Enviroment setup

import unittest
import datetime
from selenium import webdriver

class EnvironmentSetup(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome("C:\\Users\\WorkData\\Projects\\Pyselenium\\Edward\Scada\\Drivers\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)
        print("------------------------------------------------------------------")
        print("Test Environment Created")
        print("Run Started at :" + str(datetime.datetime.now()))
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def tearDown(self):
        if (self.driver!= None):
            print("------------------------------------------------------------------")
            print("Test Environment Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()


