from Demowebshop.Lib.POM.homepage import HomePage


class Digital(HomePage):
    # digital_downloads_link = ('xpath', '//a[@href="/digital-downloads"]')
    # add_to_cart = ('xpath', '//input[@value="Add to cart"]')
    # shopping_cart = ('xpath', '//span[.="Shopping cart"]')

    def digital_validate(self):
        self.click_on_digital_downloads()
        self.click_on_add_to_cart()
        self.click_on_cart()
