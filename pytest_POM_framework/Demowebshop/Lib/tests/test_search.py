import pytest

from Demowebshop.Lib.POM.homepage import HomePage
from Demowebshop.Lib.POM.searchpage import Search
from Demowebshop.Lib.tests.conftest import driver


#
#
# def test_search_laptop(driver):
#     home = HomePage(driver)
#     home.click_on_search()
#     search = Search(driver)
#     search.search_validate("laptop")
#     assert driver.find_element('xpath', '//a[.="14.1-inch Laptop"]').is_displayed()


# def test_customer_service_search(driver):
#     home = HomePage(driver)
#     home.click_on_search()
#     search = Search(driver)
#     search.search_validate()
#     assert driver.find_element('xpath', '//label[.="Search keyword:"]').is_displayed()


# def test_search_laptop(driver):
#     home = HomePage(driver)
#     home.click_on_search()
#     search = Search(driver)
#     search.search_validate("shoe")
    # assert driver.find_element('xpath', '//label[.="Category:"]').is_displayed()
    # assert driver.find_element('xpath', '//label[.="Manufacturer:"]').is_displayed()
    # assert driver.find_element('xpath', '//label[.="Price range:"]').is_displayed()
