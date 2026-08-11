import os
from collections.abc import Generator

import pytest

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


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Хук, который вызывается после каждого этапа теста. Работает даже без @allure.step в тесте."""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            AllureReporter.attach_on_failure(page, item.name)
