from playwright.sync_api import Page
import allure

from pages.github.ci_cd_page import CiCdPage


class SolutionsMenu:

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Click CI/CD link")
    def select_ci_cd(self) -> CiCdPage:
        self.page.get_by_role("link", name="CI/CD").click()
        return CiCdPage(self.page, self.page.url)
