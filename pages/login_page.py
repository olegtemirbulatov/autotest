from playwright.sync_api import expect
from pages.base_page import BasePage


class LoginPage(BasePage):

    def login(self, username: str, password: str):
        self.page.get_by_role("link", name="Sign in").click()
        self.page.locator("#login_field").fill(username)
        self.page.locator("#password").fill(password)
        self.page.get_by_role("button", name="Sign in").click()
        return self
    
    def expect_login_succeeded(self):
        expect(self.page.locator("span.styles-module__contextCrumbLast__tI2e3")).to_be_visible()

    def expect_login_failed(self):
        expect(self.page.get_by_text("Incorrect username or password")).to_be_visible()
