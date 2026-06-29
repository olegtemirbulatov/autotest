from pages.base_page import BasePage
from pages.components.solutions_menu import SolutionsMenu
from pages.topics_page import TopicsPage
from pages.login_page import LoginPage


class HomePage(BasePage):

    def go_to_solutions(self):
        self.page.get_by_role("button", name="Solutions").hover()
        return SolutionsMenu(self.page)
    
    def go_to_topics(self):
        self.page.get_by_role("button", name="Open Source", exact=True).hover()
        self.page.get_by_role("link", name="Topics").click()
        return TopicsPage(self.page, self.page.url)
    
    def go_to_login(self):
        self.page.get_by_role("link", name="Sign in").click()
        return LoginPage(self.page, self.page.url)
