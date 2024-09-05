# from Demowebshop.Lib.POM.registerpage import Register
# from Demowebshop.Lib.POM.homepage import HomePage
#
#
# def test_register_with_valid_values(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account('Jaya', 'Polanki', 'PJaya@gmail.com', 'PJaya123', 'PJaya123')
#     assert driver.find_element('xpath', '//input[@value="Continue"]').is_displayed()
#
#
# def test_register_with_existed_mail(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account('Mounika', 'Polanki', 'Pmounika@gmail.com', 'Pmouni123', 'Pmouni123')
#     assert driver.find_element('xpath', '//li[.="The specified email already exists"]').is_displayed()
#
#
# def test_register_with_no_mail(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account('Mounika', 'Polanki', '', 'Pmouni123', 'Pmouni123')
#     assert driver.find_element('xpath', '//span[.="Email is required."]').is_displayed()
#
#
# def test_register_with_no_password(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account('Mounika', 'Polanki', 'Pmounika@gmail.com', '', 'Pmouni123')
#     assert driver.find_element('xpath', '//span[.="Password is required."]').is_displayed()
#
#
# def test_register_with_no_firstname(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account('', 'Polanki', 'Pmounika@gmail.com', 'Pmouni123', 'Pmouni123')
#     assert driver.find_element('xpath', '//span[.="First name is required."]').is_displayed()
#
#
# def test_register_with_no_lastname(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account('Mounika', '', 'Pmounika@gmail.com', 'Pmouni123', 'Pmouni123')
#     assert driver.find_element('xpath', '//span[.="Last name is required."]').is_displayed()
#
#
# def test_register_with_improper_mail(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account('Mounika', 'Polanki', 'Pmounika.com', 'Pmouni123', 'Pmouni123')
#     assert driver.find_element('xpath', '//span[.="Wrong email."]').is_displayed()
#
#
# def test_register_with_lessthan_8characters(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account('Mounika', 'Polanki', 'Pmounika@gmail.com', '123', '123')
#     assert driver.find_element('xpath', '//span[.="The password should have at least 6 characters."]').is_displayed()
#
#
# def test_register_with_no_confirm_password(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_an_account('Mounika', 'Polanki', 'Pmounika@gmail.com', 'Pmouni123', '')
#     assert driver.find_element('xpath', '//span[.="Password is required."]').is_displayed()
#
#
#
