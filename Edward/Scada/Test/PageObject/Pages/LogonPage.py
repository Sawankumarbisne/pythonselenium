# Logon Page of Edward scada web application

from Test.PageObject.Locators.PageLocators import Locator
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver

class LogonPage(object):
        def __init__(self, driver):
            self.driver = driver
            # logonpage locator defining
            self.Username = driver.find_element(By.XPATH, Locator.Username)
            self.Password = driver.find_element(By.XPATH, Locator.Password)

        def getUsername(self, username):
            self.Username.clear()
            self.Username.send_keys(username)

        def getPassword(self, password):
            self.Password.clear()
            self.Password.send_keys(password)