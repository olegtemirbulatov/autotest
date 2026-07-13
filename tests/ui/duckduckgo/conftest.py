import pytest
from playwright.sync_api import Page

from pages.duckduckgo.search_page import SearchPage

DDG_URL = "https://duckduckgo.com/"


@pytest.fixture()
def ddg_search_page(page: Page):
    yield SearchPage(page, DDG_URL)
