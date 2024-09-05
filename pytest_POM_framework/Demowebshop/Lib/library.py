from selenium.webdriver import ActionChains


class Base:
    def __init__(self, driver):
        self.driver = driver

    def search_for_an_element(self, locator):
        element = self.driver.find_element(*locator)
        return element

    def click_on_an_element(self, locator):
        ele = self.search_for_an_element(locator)
        ele.click()

    def double_click_on_an_element(self, locator):
        actions = ActionChains(self.driver)
        element = self.search_for_an_element(locator)
        actions.double_click(element).perform()

    def send_text_to_an_element(self, locator, text):
        ele = self.search_for_an_element(locator)
        ele.send_keys(text)

    def click_on_checkbox(self, locator):
        ele = self.search_for_an_element(locator)
        ele.click()

    def switch_to_another_frame(self, locator):
        element = self.search_for_an_element(locator)
        self.driver.switch_to_iframe(element)
