# Recording the screen shot of each tes


from selenium import webdriver
class SS(object):

    def __init__(self, driver):
        self.driver = driver

    def ScreenShot(self, path):
        directory = ""
        self.driver.get_screenshot_as_file(directory + path)