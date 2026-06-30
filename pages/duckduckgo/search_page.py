from playwright.sync_api import expect

from pages.base_page import BasePage


class SearchPage(BasePage):

    def search(self, query: str):
        self.page.get_by_role("combobox", name="Поиск в DuckDuckGo").click()
        self.page.get_by_role("combobox", name="Поиск в DuckDuckGo").fill(query)
        self.page.get_by_test_id("searchbox-form").locator("button").filter(
            has_text="Поиск"
        ).click()
        return self

    def expect_search_results(self):
        expect(
            self.page.locator("a[data-testid='result-extras-site-search-link']").first
        ).to_be_visible()
        return self

    def get_search_results_count(self) -> int:
        headings = self.page.locator("a[data-testid='result-extras-site-search-link']")
        return headings.count()
