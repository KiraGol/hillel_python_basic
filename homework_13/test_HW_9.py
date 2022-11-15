from unittest import TestCase
from HW_9 import Bank_account
from uuid import UUID, uuid4
from datetime import date


class TestHW9(TestCase):

    def setUp(self):
        self.Bank_account = Bank_account("name_of_acc", uuid4(), 0.00)

    def test_deposit(self):
        self.assertEqual(self.Bank_account.deposit(100), [f'Sum: 100, type_of_transaction: deposit, date: {date.today()}'])

    def test_cash_withdrawal(self):
        self.assertEqual(self.Bank_account.cash_withdrawal(100), [f'Sum: 100, type_of_transaction: cash_withdrawal, date: {date.today()}'])

    def test_get_balance(self):
        self.assertEqual(self.Bank_account.get_balance(), 0)
