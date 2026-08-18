import allure
from playwright.sync_api import Page


class AllureReporter:

    @staticmethod
    def attach_on_failure(page: Page, test_name: str) -> None:
        screenshot = page.screenshot(full_page=True)
        allure.attach(
            screenshot,
            name=f"screenshot_{test_name}",
            attachment_type=allure.attachment_type.PNG,
        )
        allure.attach(
            page.content(),
            name="page_html",
            attachment_type=allure.attachment_type.HTML,
        )
