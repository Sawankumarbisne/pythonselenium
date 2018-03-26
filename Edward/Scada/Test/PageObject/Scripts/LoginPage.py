
import unittest
from Test.PageObject.TestBase.EnvironmentSetup import EnvironmentSetup
from Test.PageObject.Pages.LogonPage import LogonPage
from Test.PageObject.TestUtility.ScreenShot import SS
from Test.PageObject.Config.Globalconstant import alist
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import selenium.common.exceptions
class LoginPage(EnvironmentSetup):

    def test_ajaxcontrol(self):
        ss_path = alist[3]
        driver = self.driver
        self.driver.get(alist[0])
      #  self.driver.set_page_load_timeout(20)
      #  login = LogonPage(driver)
      #  login.getUsername(alist[1])
       # login.getPassword(alist[2])
        # Wait for grid to appear * /
        container =(By.CSS_SELECTOR,".demo-container")
        wait =WebDriverWait(driver, 5)
        wait.until(EC.presence_of_all_elements_located(container))
        # Get the text before performing an ajax call
        noDatesTextElement = driver.find_element(By.XPATH,"//div[@class='RadAjaxPanel']/span")
        textBeforeAjaxCall = noDatesTextElement.text.strip()
        # Click on the date
        driver.find_element(By.LINK_TEXT,"1").click()
        #Wait for loader to disappear
        loader =(By.CLASS_NAME,"raDiv")
        wait.until(EC.invisibility_of_element_located(loader))
        # Get the  text after  ajax call
        selectedDatesTextElement = driver.find_element(By.XPATH,"//div[@class='RadAjaxPanel']/span")
        wait.until(EC.visibility_of(selectedDatesTextElement))
        textAfterAjaxCall = selectedDatesTextElement.text.strip()
        # Verify both texts before ajax  call and after ajax call text.
        self.assertNotEqual(textBeforeAjaxCall, textAfterAjaxCall)
        expectedTextAfterAjaxCall = "Thursday, March 01, 2018"
        # Verify expected  text with text updated after ajax call
        self.assertEqual(textAfterAjaxCall, expectedTextAfterAjaxCall)
        print("Test run successfully")
      #  self.driver.implicitly_wait(20)

    def  safeJavaScriptclick(element):
        try:
          if(element.isEnabled() && element.isDisplayed())
            print("Click on element with using java script click")
            ((JavascriptExecutor) driver).executeScript("arguments[0].click();", element)
          else
            print("Unable to click on element")

        except StaleElementReferenceException as e:
                 print("Element is not attached to the page document " + e.getStackTrace())
        except Exception as e:
                 print("Unable to click on element " + e.getStackTrace())


    def test_javascriptexecuter(self):
        ss_path = alist[4]
        driver = self.driver
        self.driver.get(alist[0])
        searchtext=driver.find_element(By.id("twotabsearchtextbox"))
        searchtext.send_keys("Mobiles")
        gobutton= driver.find_element(By.CSS_SELECTOR("input[value=Go]"))
        safeJavaScriptclick(gobutton)






if __name__ == '__main__':
   unittest.main()



