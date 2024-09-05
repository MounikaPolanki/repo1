from Demowebshop.Lib.POM.homepage import HomePage


class NewsLetter(HomePage):
    email_id = ('id', 'newsletter-email')
    submit = ('id', 'newsletter-subscribe-button')

    def email_validate(self, text):
        self.click_on_an_element(self.email_id)
        self.send_text_to_an_element(self.email_id, text)
        self.click_on_an_element(self.submit)
