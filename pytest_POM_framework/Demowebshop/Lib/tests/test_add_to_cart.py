import allure
from allure_commons.types import AttachmentType

from Demowebshop.Lib.POM.digital_downloads import Digital
from Demowebshop.Lib.POM.homepage import HomePage
from Demowebshop.Lib.tests.conftest import driver


def test_digital_downloads(driver):
    home = HomePage(driver)
    home.click_on_search()
    link = Digital(driver)
    link.click_on_digital_downloads()
    # link.click_on_add_to_cart()
    assert driver.find_element('xpath', '//img[@title="Show details for Music 2"]').is_displayed()


# def test_add_to_cart(driver):
#     home = HomePage(driver)
#     home.click_on_search()
#     link = Digital(driver)
#     # link.click_on_digital_downloads()
#     link.click_on_add_to_cart()
#     assert driver.find_element('xpath', '//div[@class="bar-notification success"]').is_displayed()


def test_cart(driver):
    home = HomePage(driver)
    home.click_on_search()
    link = Digital(driver)
    link.click_on_cart()
    allure.attach(driver.get_screenshot_as_png(), name="test_cart.png", attachment_type=AttachmentType.PNG)
    assert driver.find_element('xpath', '//div[@class="order-summary-content"]').is_displayed()

##########            If condition fails       #################
# condition = driver.find_element('xpath', '//div[@class="order-summary-content"]').is_displayed()
# if not condition:
#     allure.attach(driver.get_screenshot_as_png(), name="test_cart.png", attachment_type=AttachmentType.PNG)
# assert condition
