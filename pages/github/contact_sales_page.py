import allure
from playwright.sync_api import Locator, expect

from pages.base_page import BasePage


class ContactSalesPage(BasePage):

    @property
    def first_name_input(self) -> Locator:
        return self.page.get_by_role("textbox", name="First name")

    @property
    def last_name_input(self) -> Locator:
        return self.page.get_by_role("textbox", name="Last name")

    @allure.step("Filling form (first and last names)")
    def fill_form(self, first_name: str, last_name: str) -> None:
        self.first_name_input.wait_for(state="visible")
        self.last_name_input.wait_for(state="visible")
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)

    @allure.step("Expect form filled")
    def expect_form_filled(self, first_name: str, last_name: str) -> None:
        expect(self.page.get_by_role("textbox", name="First name")).to_have_value(
            first_name
        )
        expect(self.page.get_by_role("textbox", name="Last name")).to_have_value(
            last_name
        )
