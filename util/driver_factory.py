from appium import webdriver
desired_caps = {
    "udid": "52007fb4feb33549",
    "platformName": "Android",
    "version" : "10.0",
}

class DriverFactory:
    def create_driver(self):
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return driver