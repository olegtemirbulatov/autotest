import os
from collections.abc import Generator

import pytest
from playwright.sync_api import Page
from pluggy import Result

from tests.bank_account import BankAccount
from utils.allure_reporter import AllureReporter


# OTHER
@pytest.fixture()
def account() -> BankAccount:
    return BankAccount("Ivan", 1000)


@pytest.fixture(autouse=True)
def printing_autouse_flag() -> Generator[None, None, None]:
    print("Before test")
    yield
    print("After test")


@pytest.fixture()
def output_file() -> Generator[str, None, None]:
    filename = "./test.txt"
    with open(filename, "+a") as file:
        file.write("Before test\n")
    yield filename
    with open(filename, "+a") as file:
        file.write("After test\n\n")


@pytest.fixture()
def login_credentials() -> Generator[dict[str, str | None], None, None]:
    payload = {"username": os.getenv("username"), "password": os.getenv("password")}
    yield payload


def pytest_collection_modifyitems(
    config: pytest.Config, items: list[pytest.Item]
) -> None:
    """
    Скипает тесты с меткой @pytest.mark.headed_only, если запуск идёт без --headed.
    Причина: некоторые сайты (например DuckDuckGo) показывают капчу
    при детекте headless-браузера, из-за чего тест падает не по вине кода.
    """
    if not config.getoption("--headed"):
        skip_headless = pytest.mark.skip(
            reason="Требуется --headed: сайт показывает капчу в headless-режиме"
        )
        for item in items:
            if "headed_only" in item.keywords:
                item.add_marker(skip_headless)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(
    item: pytest.Function, call: pytest.CallInfo[None]
) -> Generator[None, Result[pytest.TestReport], None]:
    """
    Хук, который вызывается после каждого этапа теста.
    Работает даже без @allure.step в тесте.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if isinstance(page, Page):
            AllureReporter.attach_on_failure(page, item.name)
