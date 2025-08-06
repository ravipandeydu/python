class Account:
    """
    A base class for bank accounts with common functionalities.
    It includes class-level attributes for bank-wide settings.
    """

    # Class variables shared across all instances
    bank_name = "National Bank"
    _total_accounts = 0
    _minimum_balance = 50

    def __init__(self, account_number, owner_name, balance=0):
        """
        Initializes a new Account instance.

        Args:
            account_number (str): The unique account number.
            owner_name (str): The name of the account owner.
            balance (float): The initial balance.

        Raises:
            ValueError: If initial balance is negative or owner name is empty.
        """
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        if not owner_name.strip():
            raise ValueError("Owner name cannot be empty.")

        self._account_number = account_number
        self._owner_name = owner_name
        self._balance = balance
        Account._total_accounts += 1

    def deposit(self, amount):
        """Adds a specified amount to the account balance."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        return f"Deposited ${amount}. New balance: ${self._balance}"

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account balance.

        Returns:
            A success message or an insufficient funds message.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self._balance - amount < self._minimum_balance:
            return "Withdrawal failed: Insufficient funds to maintain minimum balance."
        self._balance -= amount
        return f"Withdrew ${amount}. New balance: ${self._balance}"

    def get_balance(self):
        """Returns the current account balance."""
        return self._balance

    def __str__(self):
        """String representation of the account."""
        return f"[{self.__class__.__name__}] Account: {self._account_number}, Owner: {self._owner_name}, Balance: ${self._balance}"

    @classmethod
    def get_total_accounts(cls):
        """Returns the total number of accounts created."""
        return cls._total_accounts

    @classmethod
    def set_bank_name(cls, name):
        """Sets the bank name for all accounts."""
        cls.bank_name = name

    @classmethod
    def set_minimum_balance(cls, amount):
        """Sets the minimum balance requirement for all accounts."""
        if amount < 0:
            raise ValueError("Minimum balance cannot be negative.")
        cls._minimum_balance = amount


class SavingsAccount(Account):
    """A savings account with interest calculation functionality."""

    def __init__(self, account_number, owner_name, balance=0, interest_rate=0.0):
        super().__init__(account_number, owner_name, balance)
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        self.interest_rate = interest_rate

    def calculate_monthly_interest(self):
        """Calculates and deposits the monthly interest."""
        interest_earned = self.get_balance() * (self.interest_rate / 100 / 12)
        self.deposit(interest_earned)
        return interest_earned


class CheckingAccount(Account):
    """A checking account with overdraft protection."""

    def __init__(self, account_number, owner_name, balance=0, overdraft_limit=0):
        super().__init__(account_number, owner_name, balance)
        if overdraft_limit < 0:
            raise ValueError("Overdraft limit cannot be negative.")
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """
        Overrides the withdraw method to include overdraft protection.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        # Check if the withdrawal exceeds the balance plus the overdraft limit
        if self._balance - amount < -self.overdraft_limit:
            return "Withdrawal failed: Exceeds overdraft limit."

        self._balance -= amount
        return f"Withdrew ${amount}. New balance: ${self._balance}"


# --- Test Cases ---

# Test Case 1: Creating different types of accounts
savings_account = SavingsAccount("SA001", "Alice Johnson", 1000, 2.5)
checking_account = CheckingAccount("CA001", "Bob Smith", 500, 200)

print(f"Savings Account: {savings_account}")
print(f"Checking Account: {checking_account}")
print("-" * 30)

# Test Case 2: Deposit and Withdrawal operations
print(f"Savings balance before: ${savings_account.get_balance()}")
savings_account.deposit(500)
print(f"After depositing $500: ${savings_account.get_balance()}")

withdrawal_result = savings_account.withdraw(200)
print(f"Withdrawal result: {withdrawal_result}")
print(f"Balance after withdrawal: ${savings_account.get_balance()}")
print("-" * 30)

# Test Case 3: Overdraft protection in checking account
print(f"Checking balance: ${checking_account.get_balance()}")
# This withdrawal should use the overdraft
overdraft_result = checking_account.withdraw(600)
print(f"Overdraft withdrawal: {overdraft_result}")
print(f"Balance after overdraft: ${checking_account.get_balance()}")
print("-" * 30)

# Test Case 4: Interest calculation for savings
interest_earned = savings_account.calculate_monthly_interest()
print(f"Monthly interest earned: ${interest_earned:.2f}")
print(f"Balance after interest: ${savings_account.get_balance():.2f}")
print("-" * 30)

# Test Case 5: Class methods and variables
print(f"Total accounts created: {Account.get_total_accounts()}")
print(f"Bank name: {Account.bank_name}")

# Change bank settings using class method
Account.set_bank_name("New National Bank")
Account.set_minimum_balance(100)
print(f"Updated Bank name: {Account.bank_name}")
print(f"Updated Minimum Balance: {Account._minimum_balance}")
print("-" * 30)

# Test Case 6: Account validation
try:
    # This should raise a ValueError
    invalid_account = SavingsAccount("SA002", "", -100, 1.5)
except ValueError as e:
    print(f"Validation error: {e}")

try:
    # This should also raise a ValueError
    savings_account.deposit(-50)
except ValueError as e:
    print(f"Validation error: {e}")
