class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account balance."""
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount <= 0:
            return "Deposit amount must be greater than zero."
        self._account_balance += amount
        return f"Deposited: ${amount:.2f}"

    def withdraw(self, amount):
        """Withdraw a specified amount if funds are sufficient."""
        if amount <= 0:
            return "Withdrawal amount must be greater than zero."
        if amount > self._account_balance:
            return False  # Insufficient funds
        self._account_balance -= amount
        return True

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self._account_balance:.2f}")

