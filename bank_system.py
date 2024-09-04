from datetime import datetime

# Define bank accounts dictionary
bank_accounts = {
    1001: {
        "first_name": "Alice",
        "last_name": "Smith",
        "id_number": "123456789",
        "balance": 2500.50,
        "transactions_to_execute": [
            ("2024-08-17 14:00:00", 1001, 1002, 300),
            ("2024-08-17 15:00:00", 1001, 1003, 200)
        ],
        "transaction_history": [
            ("2024-08-15 09:00:00", 1001, 1002, 500, "2024-08-15 09:30:00")
        ]
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


def perform_trx(trx_account_number):
    """
    Perform all pending transactions for the given account.
    """
    account = bank_accounts.get(trx_account_number)

    if account:
        while account["transactions_to_execute"]:
            trx = account["transactions_to_execute"].pop(0)  # Perform the first pending transaction
            trx_time, source_acc, target_acc, amount = trx

            if bank_accounts[source_acc]["balance"] >= amount:
                bank_accounts[source_acc]["balance"] -= amount
                bank_accounts[target_acc]["balance"] += amount
                account["transaction_history"].append(
                    (trx_time, source_acc, target_acc, amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                )
            else:
                print(f"Insufficient balance in account {source_acc} to perform transaction of {amount}.")
    else:
        print(f"Account {trx_account_number} does not exist.")


def create_trx(trx_account_number, target_acc, amount):
    """
    Create a new transaction for the given account.
    """
    account = bank_accounts.get(trx_account_number)

    if account:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        account["transactions_to_execute"].append(
            (current_time, trx_account_number, target_acc, amount)
        )
        print(f"Transaction created: {trx_account_number} -> {target_acc} : {amount}")
    else:
        print(f"Account {trx_account_number} does not exist.")


def get_by_name(name):
    """
    Get all accounts that match the given name.
    """
    matched_accounts = []
    for account_number, account_details in bank_accounts.items():
        if name.lower() in account_details["first_name"].lower():
            matched_accounts.append(account_details)
    return matched_accounts


def print_account_details(account_number):
    """
    Print details of a specific account.
    """
    account = bank_accounts.get(account_number)
    if account:
        print(f"Account {account_number}:")
        print(f"  Name: {account['first_name']} {account['last_name']}")
        print(f"  ID Number: {account['id_number']}")
        print(f"  Balance: {account['balance']}")
        print(f"  Pending Transactions: {account['transactions_to_execute']}")
        print(f"  Transaction History: {account['transaction_history']}")
    else:
        print(f"Account {account_number} does not exist.")


def main_menu():
    """
    Main menu for user interaction.
    """
    while True:
        print("\nBank System Menu:")
        print("1. Add new transaction")
        print("2. Perform all pending transactions for an account")
        print("3. Show account details")
        print("4. Search accounts by first name")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            account_number = int(input("Enter source account number: "))
            target_account = int(input("Enter target account number: "))
            amount = float(input("Enter amount to transfer: "))
            create_trx(account_number, target_account, amount)
        elif choice == '2':
            account_number = int(input("Enter account number to perform transactions: "))
            perform_trx(account_number)
        elif choice == '3':
            account_number = int(input("Enter account number to show details: "))
            print_account_details(account_number)
        elif choice == '4':
            name = input("Enter the first name to search: ")
            accounts = get_by_name(name)
            for account in accounts:
                print_account_details(account)
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please select from 1 to 5.")


if __name__ == "__main__":
    main_menu()
