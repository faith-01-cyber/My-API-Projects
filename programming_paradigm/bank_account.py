class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a new BankAccount instance.
        :param initial_balance: Starting balance (default 0)
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Add money to the account balance.
        :param amount: float
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deduct money from the account balance if sufficient funds exist.
        :param amount: float
        :return: True if withdrawal successful, False if insufficient funds
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Print the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance}")





