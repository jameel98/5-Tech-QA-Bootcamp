# main.py

from bank import BankAccount

if __name__ == '__main__':
    # Create an instance of the BankAccount class
    acc_num = input("Enter your account number: ")
    account = BankAccount(account_number=acc_num)

    while True:
        print("\nChoose an option:")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Check balance")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            # Deposit money
            try:
                deposit_money = float(input("Enter amount to deposit: "))
                account.deposit(deposit_money)
                print(f"Deposited {deposit_money}, current balance: {account.get_balance()}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            # Withdraw money
            try:
                withdraw_amount = float(input("Enter amount to withdraw: "))
                if account.get_balance() >= withdraw_amount:
                    account.withdraw(withdraw_amount)
                    print(f"Withdrew {withdraw_amount}, current balance: {account.get_balance()}")
                else:
                    print(f"Not enough funds. Current balance: {account.get_balance()}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '3':
            # Check balance
            current_balance = account.get_balance()
            print(f"Current balance: {current_balance}")

        elif choice == '4':
            # Exit
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")
