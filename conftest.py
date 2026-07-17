import os
from collections.abc import Generator

import pytest

from tests.bank_account import BankAccount


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
