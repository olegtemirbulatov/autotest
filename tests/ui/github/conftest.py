import os
from collections.abc import Generator
from typing import Tuple

import pytest
from dotenv import load_dotenv
from faker import Faker
from playwright.sync_api import Page

from pages.github.home_page import HomePage

GITHUB_URL = "https://github.com/"
load_dotenv()


@pytest.fixture()
def github_home_page(page: Page) -> Generator[HomePage, None, None]:
    yield HomePage(page, GITHUB_URL)


@pytest.fixture()
def gh_credentials() -> Generator[Tuple[str | None, str | None], None, None]:
    yield os.getenv("GH_USER"), os.getenv("GH_PASS")


@pytest.fixture()
def faker() -> Generator[Faker, None, None]:
    yield Faker()
