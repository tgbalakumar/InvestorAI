import logging
from util.element import Element
from appium.webdriver.common.mobileby import MobileBy

logger=logging.getLogger(__name__)

class LoginPage:
    """ This is the login page"""
    def __init__(self, driver):
        self.driver=driver
        self.element=Element()

    def login_to_home_page(self):
        password_input=self.element.get_element(self.driver, "//android.widget.FrameLayout/android.widget.EditText")
        password_input.send_keys("625001")
        signin_btn=self.element.get_element(self.driver, "com.bridgeweave.investorai:id/layout_SignIn", MobileBy.ID)
        signin_btn.click()

    def skip_onboarding_page(self):
        skip_btn=self.element.get_element(self.driver, "com.bridgeweave.investorai:id/skip", MobileBy.ID)
        skip_btn.click()

