from typing import Self

from playwright.sync_api import expect

from pages.base_page import BasePage


class LoginPage(BasePage):

    def login(self, username: str, password: str) -> Self:
        self.page.get_by_label("Username").fill(username)
        self.page.get_by_label("Password").fill(password)
        self.page.get_by_role("button", name="Sign in").click()
        return self

    def expect_login_succeeded(self) -> None:
        expect(self.page.get_by_test_id("github-avatar")).to_be_visible()

    def expect_login_failed(self) -> None:
        expect(self.page.get_by_role("alert")).to_be_visible()
