import pytest

from tests.bank_account import BankAccount


@pytest.mark.skip
@pytest.mark.parametrize(
    "balance, account_balance", [(-1, ValueError), (0, 1000), (1, 999)]
)
def test_withdraw(
    account: BankAccount,
    output_file: str,
    balance: int,
    account_balance: int | type[ValueError],
) -> None:
    if account_balance is ValueError:
        with pytest.raises(ValueError):
            account.withdraw(balance)
    else:
        account.withdraw(balance)
        assert account.balance == account_balance
    with open(output_file, "+a") as file:
        file.write(
            f"test_withdraw\nbalance = {balance}, account_balance = {account_balance}\n"
        )


@pytest.mark.skip
@pytest.mark.parametrize(
    "balance, account_balance", [(-1, ValueError), (0, 1000), (1, 1001)]
)
def test_deposit(
    account: BankAccount,
    output_file: str,
    balance: int,
    account_balance: int | type[ValueError],
) -> None:
    if account_balance is ValueError:
        with pytest.raises(ValueError):
            account.deposit(balance)
    else:
        account.deposit(balance)
        assert account.balance == account_balance
    with open(output_file, "+a") as file:
        file.write(
            f"test_deposit\nbalance = {balance}, account_balance = {account_balance}\n"
        )
