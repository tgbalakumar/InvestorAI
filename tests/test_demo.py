
import logging
from util.base_test import BaseTest

logger=logging.getLogger(__name__)

class TestDemo(BaseTest):
    def test_demo(self):
        self.driver.terminate_app("com.bridgeweave.investorai")
        self.driver.activate_app("com.bridgeweave.investorai")
        self.investorai.login.login_to_home_page()
        self.investorai.login.skip_onboarding_page()
        self.investorai.search_and_result.input_search("Apple Inc")
        logger.info(self.investorai.search_and_result.get_result())
        self.driver.execute_script('mobile: shell', {"command": 'input keyevent 4'})
        self.investorai.search_and_result.input_search("Tesla Inc")
        logger.info(self.investorai.search_and_result.get_result())





(x=346, y=585).perform()
# inputB = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((MobileBy.ID, "com.bridgeweave.investorai:id/tvPrice")))
# print(inputB.text)
# driver.quit()