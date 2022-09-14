# Описати клас "Банківський рахунок", атрибути якого:
#
#    - ім'я облікового запису - str
#    - унікальний id (uuid)
#    - баланс float (чи Decimal)
#    - транзакції (список)
#    Методи
#
#      депозит коштів
#      виведення коштів
#      отримати баланс
#
#
#    При зміні балансу записувати в транзакції (сума, тип операції, поточна_дата)
#
#    * Дод. додати та враховувати банківські комісії (1%)
from datetime import date
from uuid import UUID, uuid4


class Bank_account:
    def __init__(
            self,
            account_name: str,
            id: UUID,
            balance: float,
            transactions: list = None,
    ):
        self.account_name = account_name
        self.id = id
        self.balance = balance
        self.transactions = transactions

    def deposit(self, sum_of_deposit: float):
        """put money on deposit"""
        self.transactions = []
        self.balance = self.balance + sum_of_deposit - sum_of_deposit * 0.01
        self.transactions.append(f"Sum: {sum_of_deposit}, "
                                 f"type_of_transaction: deposit, "
                                 f"date: {date.today()}")
        return self.transactions

    def cash_withdrawal(self, sum_of_cash: float):
        """withdraw cash from an account"""
        self.balance = self.balance - sum_of_cash - sum_of_cash * 0.01
        self.transactions.append(f"Sum: {sum_of_cash}, type_of_transaction: "
                                 f"cash_withdrawal, date: {date.today()}")
        return self.transactions

    def get_balance(self):
        """return current balance"""
        return self.balance

    def get_transactions(self):
        """return list of transaction"""
        return self.transactions


if __name__ == '__main__':
    some_acc = Bank_account("name_of_acc", uuid4(), 0.00)
    print(some_acc.deposit(300.00))
    print(some_acc.cash_withdrawal(100))
    print(some_acc.transactions)
    print(some_acc.get_balance())
    print(some_acc.get_transactions())
