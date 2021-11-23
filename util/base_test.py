import logging
import pytest
import conftest
from page_objects.investorai import InvestorAI

logger=logging.getLogger(__name__)

@pytest.mark.usefixtures("common_fixture")
class BaseTest:
    @pytest.fixture(scope="function")
    def common_fixture(self, request, driver_fixture):
        logger.info("inside base fixture")
        self.driver=request.cls.driver
        self.investorai=InvestorAI(self.driver)
