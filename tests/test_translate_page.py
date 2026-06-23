# from playwright.sync_api import Page, expect
import pytest
from pages.translate_page import TranslatePage


@pytest.mark.ui
def test_open(translate_page: TranslatePage):
    assert "translate.google.com" in translate_page.page.url