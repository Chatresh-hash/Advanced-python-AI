"""
In this example:

We have a base class BankAccount representing a generic bank account with methods for depositing, withdrawing, and displaying the balance.
We define a subclass SavingsAccount that inherits from BankAccount. This subclass overrides the withdraw method to apply a withdrawal 
fee specific to savings accounts.
Inside the SavingsAccount class, we override the withdraw method to include the withdrawal fee calculation and call the parent 
class's withdraw method using super() to handle the actual withdrawal.
We create instances of both BankAccount and SavingsAccount and demonstrate depositing, withdrawing, and displaying the 
balances for each account.
This example showcases method overriding in the context of a bank account system and demonstrates how the self parameter is used 
to access instance attributes and call methods within class definitions.
"""
class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):  #super_class
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Account balance for {self.owner_name}: ${self.balance}")

# Subclass SavingsAccount inheriting from BankAccount
class SavingsAccount(BankAccount): #Single Inheritance
    def withdraw(self, amount):   # subclass
        # Check if withdrawal amount exceeds balance
        if amount <= self.balance:
            # Apply withdrawal fee for savings account
            withdrawal_fee = 0.02 * amount
            amount+= withdrawal_fee
            # Call parent class's withdraw method
            super().withdraw(amount)  #Method overrding
            print(f"Withdrawal fee: ${withdrawal_fee}")
        else:
            print("Insufficient funds.")

# Create instances of BankAccount and SavingsAccount
bank_acc = BankAccount("123456", "Dilip", 10000)
savings_acc = SavingsAccount("789012", "Arya", 2000)
current_acc = BankAccount("345678", "John", 5000)

# Deposit into bank account
bank_acc.deposit(2000)

# Withdraw from bank account
bank_acc.withdraw(3000)

# Display bank account balance
bank_acc.display_balance()

# Deposit into savings account
savings_acc.deposit(1000)

# Withdraw from savings account
savings_acc.withdraw(500)  # Subclass

# Display savings account balance
display_balance = savings_acc.display_balance()
display_balance = current_acc.display_balance()