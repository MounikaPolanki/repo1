from Demowebshop.Lib.library import Base


class HomePage(Base):
    login_link_locator = ("xpath", "//a[.='Log in']")
    register_link_locator = ("xpath", "//a[.='Register']")
    search_link_locator = ('xpath', '//input[@id="small-searchterms"]')
    digital_downloads_locator = ('xpath', '//a[@href="/digital-downloads"]')
    add_to_cart_locator = ('xpath', '//div[@class="prices"]/span[text()="1.00"]/../../div[@class="buttons"]//input['
                                    '@value="Add to cart"]')
    shopping_cart_locator = ('xpath', '//span[.="Shopping cart"]')
    news_letter = ('xpath', '//input[@id="newsletter-email"]')
    customer_service = ('xpath', '//a[@href="/search"]')

    def click_on_login(self):
        self.click_on_an_element(self.login_link_locator)

    def click_on_register(self):
        self.click_on_an_element(self.register_link_locator)

    def click_on_search(self):
        self.click_on_an_element(self.search_link_locator)

    def send_text_to_an_element(self, locator, text):
        ele = self.search_for_an_element(locator)
        ele.send_keys(text)

    def click_on_digital_downloads(self):
        self.click_on_an_element(self.digital_downloads_locator)

    def click_on_add_to_cart(self):
        self.click_on_an_element(self.add_to_cart_locator)

    def click_on_cart(self):
        self.click_on_an_element(self.shopping_cart_locator)

    def click_on_news_letter(self):
        self.click_on_an_element(self.news_letter)

    def click_on_customer_search(self):
        self.click_on_an_element(self.customer_service)

