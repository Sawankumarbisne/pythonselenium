from selenium import webdriver
from time import sleep
import unittest
import datetime
from Test.PageObject.Pages.LogonPage import LogonPage
from Test.PageObject.TestUtility.ScreenShot import SS

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\WorkData\\Projects\\Pyselenium\\Edward\Scada\\Drivers\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)
        print("------------------------------------------------------------------")
        print("Test Environment Created")
        print("Run Started at :" + str(datetime.datetime.now()))

    def test_NavigateMercury(self):
#       self.driver.get("http://newtours.demoaut.com/")
#       print(self.driver.title)
#       self.driver.get_screenshot_as_file("C:\Python\home.png")
#       self.driver.maximize_window()

        ss_path = "C:\\Users\\WorkData\\Projects\\Pyselenium\\Edward\Scada\\Drivers"
        driver = self.driver
        self.driver.get("http://160.100.28.217/EdwardsScada/")
        self.driver.set_page_load_timeout(20)
        login = LogonPage(driver)
        login.getUsername("Administrator")
        login.getPassword("toolkit")
        print("Test run successfully")
        print("Refreshing the page")
        self.driver.execute_script("history.go(0)")
        sleep(2)

        print("Page title is :"+self.driver.execute_script("return document.title;"))

        search = self.driver.execute_script("return document.getElementById('searchBtn');")
        print("Search button class :"+search.get_attribute("class"))
        sleep(2)

        print("Scrolling down to coordinates (300,2000)")
        self.driver.execute_script("window.scrollBy(300,2000)")
        sleep(2)

        print("Scrolling down to a element")
        ele = self.driver.find_element_by_xpath("//*[contains(text(),'Follow us')]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ele)
        print("Scrolled successfully to :"+ele.text)
        sleep(2)

        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", ele, "background:yellow; color: Red; border: 4px dotted solid yellow;")
        print("Highlighted elements :"+ele.text)
        sleep(2)

        twt = self.driver.find_element_by_xpath("//*[contains(text(),'Twitter')]")
        self.driver.execute_script("arguments[0].click();",twt)
        print("Clicked in Twitter link")
        sleep(2)

    def tearDown(self):
        if (self.driver!= None):
            print("------------------------------------------------------------------")
            print("Test Environment Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()

