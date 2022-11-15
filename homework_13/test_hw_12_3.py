from unittest import TestCase
from HW_12_3 import check_password


class TestHW7(TestCase):

    def test_length_of_password(self):
        assert check_password("JHfff$HJJU000677)600U)") == "Password is correct"

    def test_length_of_password_incorrect(self):
        with self.assertRaises(ValueError) as context:
            check_password("78$Lo")
        self.assertEqual('Not correct length of password', str(context.exception))

    def test_az_symbols(self):
        assert check_password("hhuLj78O$") == "Password is correct"

    def test_az_symbols_incorrect(self):
        with self.assertRaises(ValueError) as context:
            check_password("78$LLLOOOUYY")
        self.assertEqual('Do not have a-z symbols', str(context.exception))

    def test_AZ_symbols(self):
        assert check_password("hhuLj78O$") == "Password is correct"

    def test_AZ_symbols_incorrect(self):
        with self.assertRaises(ValueError) as context:
            check_password("78$kiooldjg")
        self.assertEqual('Do not have A-Z symbols', str(context.exception))

    def test_numbers(self):
        assert check_password("hhuLj78O$") == "Password is correct"

    def test_numbers_incorrect(self):
        with self.assertRaises(ValueError) as context:
            check_password("POO$kiooldjg")
        self.assertEqual('Do not have 0-9 numbers', str(context.exception))

    def test_characters(self):
        assert check_password("hhuLj78O$") == "Password is correct"

    def test_characters_incorrect(self):
        with self.assertRaises(ValueError) as context:
            check_password("POOkioo99l)))djg")
        self.assertEqual('Do not have characters in password $#-@+=', str(context.exception))


