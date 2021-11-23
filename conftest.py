from util.driver_factory import DriverFactory
import pytest
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="function")
def driver_fixture(request):
    mobile_driver=DriverFactory().create_driver()
    request.cls.driver=mobile_driver
    logger.info("inside driver fixture")
    yield
    mobile_driver.quit()
