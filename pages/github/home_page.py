import allure

from pages.base_page import BasePage
from pages.github.components.solutions_menu import SolutionsMenu
from pages.github.login_page import LoginPage
from pages.github.topics_page import TopicsPage


class HomePage(BasePage):

    @allure.step("Open solutions menu")
    def go_to_solutions(self) -> SolutionsMenu:
        self.page.get_by_role("button", name="Solutions").hover()
        return SolutionsMenu(self.page)

    @allure.step("Go to topics page")
    def go_to_topics(self) -> TopicsPage:
        self.page.get_by_role("button", name="Open Source", exact=True).hover()
        self.page.get_by_role("link", name="Topics").click()
        return TopicsPage(self.page, self.page.url)

    @allure.step("Go to login page")
    def go_to_login(self) -> LoginPage:
        self.page.get_by_role("link", name="Sign in").click()
        return LoginPage(self.page, self.page.url)
