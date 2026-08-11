from collections.abc import Generator

import pytest
import allure
from playwright.sync_api import Page

from pages.duckduckgo.search_page import SearchPage

DDG_URL = "https://duckduckgo.com/"


@pytest.fixture()
def ddg_search_page(page: Page) -> Generator[SearchPage, None, None]:
    yield SearchPage(page, DDG_URL)
