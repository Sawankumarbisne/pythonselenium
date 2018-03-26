
import os
from selenium import webdriver

#dire = os.getcwd()
ie_driver_path = "C:\\Users\\WorkData\\Projects\\Pyselenium\\Edward\\Scada\\Drivers\\IEDriverServer.exe"

# create a new Internet explorer session
driver = webdriver.Ie(ie_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://toolsqa.com/automation-practice-form/")

search_field = driver.find_element_by_name("firstname")
search_field.clear()
search_field.send_keys("Hari")

search_last = driver.find_element_by_name("lastname")
search_last.clear()
search_last.send_keys("Kumar")

sexmale = driver.find_element_by_id("sex-0")
sexmale.click()

sexfemale = driver.find_element_by_id("sex-1")
sexfemale.click()

experience = driver.find_element_by_id("exp-6")
experience.click()

datep = driver.find_element_by_id("datepicker")
datep.send_keys("08-03-2018")

tester = driver.find_element_by_id("profession-1")
tester.click()
driver.implicitly_wait(30)
driver.quit()

