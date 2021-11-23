from .login import LoginPage
from .search_and_result import SearchAndResultPage
import logging

logger=logging.getLogger(__name__)
class InvestorAI:
    def __init__(self, driver):
        self.driver = driver

    @property
    def login(self):
        """ Creates LoginPage POM"""
        logger.info("This is login page")
        return LoginPage(self.driver)

    @property
    def search_and_result(self):
        """ Creates Search and Result POM"""
        logger.info("This is search and result page")
        return SearchAndResultPage(self.driver)

