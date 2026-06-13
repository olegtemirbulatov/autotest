import pytest
from bank_account import BankAccount


@pytest.fixture
def account():
    return BankAccount("Ivan", 1000)


@pytest.mark.parametrize("balance, account_balance", [
    (-1, ValueError),
    (0, 1000),
    (1, 999)
])
def test_withdraw(account, balance, account_balance):
    if account_balance is ValueError:
        with pytest.raises(ValueError):
            account.withdraw(balance)
    else:
        account.withdraw(balance)
        assert account.balance == account_balance


@pytest.mark.parametrize("balance, account_balance", [
    (-1, ValueError),
    (0, 1000),
    (1, 1001)
])
def test_deposit(account, balance, account_balance):
    if account_balance is ValueError:
        with pytest.raises(ValueError):
            account.deposit(balance)
    else:
        account.deposit(balance)
        assert account.balance == account_balance