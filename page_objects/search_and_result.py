import logging
from util.element import Element
from appium.webdriver.common.mobileby import MobileBy
import time
from appium.webdriver.common.touch_action import TouchAction

logger=logging.getLogger(__name__)

class SearchAndResultPage:
    """ This is the Search and result page"""
    def __init__(self, driver):
        self.driver=driver
        self.element=Element()

    def input_search(self, text: str = ""):
        search_box=self.element.get_element(self.driver, "com.bridgeweave.investorai:id/etCompanyName", MobileBy.ID)
        search_box.click()
        search_box.send_keys(text[:5])
        time.sleep(2)
        search_box.send_keys(text)
        time.sleep(5)
        TouchAction(self.driver).tap(x=346, y=585).perform()

    def get_result(self):
        result=self.element.get_element(self.driver, "com.bridgeweave.investorai:id/tvPrice", MobileBy.ID)
        return result.text