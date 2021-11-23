
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
from selenium.common.exceptions import TimeoutException

class Element:
    """ This is Element class """
    def get_element(self, driver: webdriver, locator_id, locator_type=MobileBy.XPATH):
        try:
             elem=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((locator_type,locator_id)))
             return elem
        except TimeoutException:
            return False

