import pytest
from pages.duckduckgo.search_page import SearchPage
from playwright.sync_api import Page

DDG_URL = "https://duckduckgo.com/"


@pytest.fixture()
def ddg_search_page(page: Page):
    yield SearchPage(page, DDG_URL)