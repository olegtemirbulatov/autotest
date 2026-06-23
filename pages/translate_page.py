from playwright.sync_api import Page


class TranslatePage:
    URL = "https://translate.google.com/?sl=en&tl=ru&op=translate"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)
        return self
