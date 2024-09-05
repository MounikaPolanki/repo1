import allure
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture()
def driver():
    driver = WebDriver()
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    yield driver
    driver.close()
# def attach_screenshot():
#     allure.attach(driver.get_screenshot_as_png(), name="test_cart.png", attachment_type=AttachmentType.PNG)