from typing import Self
import allure

from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page, url: str) -> None:
        self.page = page
        self.url = url

    @allure.step("Opening page")
    def open(self) -> Self:
        self.page.goto(self.url)
        return self
