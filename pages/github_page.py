import re
from playwright.sync_api import Page, expect


class GithubPage:
    URL = "https://github.com/"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)
        return self
    
    def sign_in(self, username: str, password: str):
        expect(self.page.get_by_role("link", name="Sign in")).to_be_visible()
        self.page.get_by_role("link", name="Sign in").click()
        expect(self.page).to_have_url(re.compile(r"/login"))
        self.page.locator("#login_field").fill(username)
        self.page.locator("#password").fill(password)
        self.page.get_by_role("button", name="Sign in").click()
        return self