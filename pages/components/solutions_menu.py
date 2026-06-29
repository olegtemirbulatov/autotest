from playwright.sync_api import Page
from pages.ci_cd_page import CiCdPage


class SolutionsMenu:

    def __init__(self, page: Page):
        self.page = page

    def select_ci_cd(self) -> CiCdPage:
        self.page.get_by_role("link", name="CI/CD").click()
        return CiCdPage(self.page, self.page.url)
        