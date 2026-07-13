import os

import pytest
from tests.bank_account import BankAccount


# OTHER
@pytest.fixture()
def account():
    return BankAccount("Ivan", 1000)


@pytest.fixture(autouse=True)
def printing_autouse_flag():
    print("Before test")
    yield
    print("After test")


@pytest.fixture()
def output_file():
    filename = "./test.txt"
    with open(filename, "+a") as file:
        file.write("Before test\n")
    yield filename
    with open(filename, "+a") as file:
        file.write("After test\n\n")


@pytest.fixture()
def login_credentials():
    payload = {"username": os.getenv("username"), "password": os.getenv("password")}
    yield payload
