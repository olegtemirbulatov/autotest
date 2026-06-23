# from playwright.sync_api import Page, expect
from pages.translate_page import TranslatePage


def test_open(translate_page: TranslatePage):
    assert "translate.google.com" in translate_page.page.url