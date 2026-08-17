from typing import Self

import allure
from playwright.sync_api import expect

from pages.base_page import BasePage


class SearchPage(BasePage):

    @allure.step("Fill search form and click Search button")
    def search(self, query: str) -> Self:
        self.page.locator("input[id='searchbox_input']").click()
        self.page.locator("input[id='searchbox_input']").fill(query)
        self.page.locator("button[data-mode='search']").click()
        return self

    @allure.step("Expect search result")
    def expect_search_results(self) -> Self:
        expect(
            self.page.locator("a[data-testid='result-extras-site-search-link']").first
        ).to_be_visible()
        return self

    @allure.step("Count search results")
    def get_search_results_count(self) -> int:
        headings = self.page.locator("a[data-testid='result-extras-site-search-link']")
        return headings.count()
