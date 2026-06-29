from pages.base_page import BasePage
from pages.components.solutions_menu import SolutionsMenu


class HomePage(BasePage):

    def go_to_solutions(self):
        self.page.get_by_role("button", name="Solutions").hover()
        return SolutionsMenu(self.page)