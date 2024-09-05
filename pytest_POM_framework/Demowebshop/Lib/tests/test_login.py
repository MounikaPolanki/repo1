import credentials
import openpyxl
import pytest

from Demowebshop.Lib.POM.homepage import HomePage
from Demowebshop.Lib.POM.login import LogIn
from utilities.exel_reader import get_list_from_exel

#
# # usernames = ["PJaya@gmail.com", "abc@gmail.com", "xyz@yahoo.com", "mon@gmail.com", "abcd123"]
#
# # usernames = [("PJaya@gmail.com", "PJaya123"), ("abc@gmail.com", "12345"), ("xyz@yahoo.com", "123456"),
# #              ("mon@gmail.com", "abcd123")]




# print(credentials_list)


Credentials = get_list_from_exel()


# @pytest.mark.parametrize("username,password", Credentials)
# def test_login_with_proper_credentials(driver, username, password):
#     home = HomePage(driver)
#     home.click_on_login()
#     login = LogIn(driver)
#     login.login_to_the_application(username, password)
#     assert driver.find_element("xpath", f"//a[.='{username}']").is_displayed()

# @pytest.mark.skip
# def test_login_with_no_password(driver):
#     home = HomePage(driver)
#     home.click_on_login()
#     login = LogIn(driver)
#     login.login_to_the_application("pmouni@gmail.com", "")
#     assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()

#
# @pytest.mark.skip
# def test_login_with_no_username(driver):
#     home = HomePage(driver)
#     home.click_on_login()
#     login = LogIn(driver)
#     login.login_to_the_application("", "mouni123")
#     assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()
#
#
# @pytest.mark.skip
# def test_login_with_no_credntials(driver):
#     home = HomePage(driver)
#     home.click_on_login()
#     login = LogIn(driver)
#     login.login_to_the_application("", "")
#     assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()
#
#
# @pytest.mark.skip
# def test_login_with_invalid_credntials(driver):
#     home = HomePage(driver)
#     home.click_on_login()
#     login = LogIn(driver)
#     login.login_to_the_application("abc@gmail.com", "waste java")
#     assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()


# def test_login(driver):
#     home = HomePage(driver)
#     home.click_on_login()
#     login = LogIn(driver)
#     login.login_to_the_application("demoweb842@gmail.com", "demoweb12")
#     assert driver.find_element("xpath", "//span[contains(.,'Login was unsuccessful')]").is_displayed()