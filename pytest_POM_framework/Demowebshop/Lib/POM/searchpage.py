from Demowebshop.Lib.POM.homepage import HomePage


class Search(HomePage):
    search_text_field = ('id', 'small-searchterms')
    submit = ('xpath', '//input[@value="Search"]')
    advance_search = ('xpath', '//input[@value="true"]')
    # search = ('xpath', '//a[@href="/search"] ')

    def search_validate(self, text):
        self.click_on_an_element(self.search_text_field)
        self.send_text_to_an_element(self.search_text_field, text)
        self.click_on_an_element(self.submit)
        self.click_on_checkbox(self.advance_search)
        # self.click_on_an_element(self.search)

