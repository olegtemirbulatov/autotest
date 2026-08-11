from pages.base_page import BasePage
from pages.github.contact_sales_page import ContactSalesPage
import allure


class CiCdPage(BasePage):

    @allure.step("Click contact sales link")
    def click_contact_sales(self) -> ContactSalesPage:
        self.page.get_by_test_id("Hero-grid").get_by_role(
            "link", name="Contact sales"
        ).click()
        return ContactSalesPage(self.page, self.page.url)
