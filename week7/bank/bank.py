# bank.py

class BankAccount:
    def __init__(self, account_number, initial_balance=0.0):
        self._account_number = account_number
        self._balance = initial_balance

    # Property for account_number
    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        if isinstance(value, str) and value.strip():
            self._account_number = value
        else:
            raise ValueError("Account number must be a non-empty string")

    # Property for balance
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._balance = value
        else:
            raise ValueError("Balance must be a non-negative number")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
            else:
                raise ValueError("Insufficient funds")
        else:
            raise ValueError("Withdrawal amount must be positive")

    def get_balance(self):
        return self.balance
