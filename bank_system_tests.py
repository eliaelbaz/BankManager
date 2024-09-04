import unittest
from bank_system import bank_accounts, perform_trx, create_trx, get_by_name


class TestBankSystem(unittest.TestCase):

    def setUp(self):
        """
        Initialize test data before each test.
        """
        # Reset accounts for tests
        self.original_bank_accounts = {
            1001: {
                "first_name": "Alice",
                "last_name": "Smith",
                "id_number": "123456789",
                "balance": 2500.50,
                "transactions_to_execute": [],
                "transaction_history": []
            },
            1002: {
                "first_name": "Bob",
                "last_name": "Johnson",
                "id_number": "987654321",
                "balance": 3900.75,
                "transactions_to_execute": [],
                "transaction_history": []
            },
            1003: {
                "first_name": "Charlie",
                "last_name": "Brown",
                "id_number": "111222333",
                "balance": 1500.00,
                "transactions_to_execute": [],
                "transaction_history": []
            }
        }
        # Reset the global bank_accounts for each test
        bank_accounts.clear()
        bank_accounts.update(self.original_bank_accounts)

    def test_perform_trx(self):
        """
        Test performing transactions.
        """
        create_trx(1001, 1002, 300)
        perform_trx(1001)
        self.assertEqual(bank_accounts[1001]["transactions_to_execute"], [])
        self.assertEqual(bank_accounts[1001]["balance"], 2200.50)
        self.assertEqual(bank_accounts[1002]["balance"], 4200.75)

    def test_create_trx(self):
        """
        Test creating a transaction.
        """
        create_trx(1001, 1002, 150)
        self.assertEqual(len(bank_accounts[1001]["transactions_to_execute"]), 1)
        self.assertEqual(bank_accounts[1001]["transactions_to_execute"][0][1:], (1001, 1002, 150))

    def test_get_by_name(self):
        """
        Test retrieving accounts by name.
        """
        result = get_by_name("Alice")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["first_name"], "Alice")

        result = get_by_name("bo")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["first_name"], "Bob")


if __name__ == '__main__':
    unittest.main ()