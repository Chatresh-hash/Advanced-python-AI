"""
In single inheritance, a subclass inherits from only one superclass.
In the bank account example, we'll create a SavingsAccount class that inherits from
the BankAccount class.
"""


#1. Define the Base Class (`BankAccount`):
#   - Create a class `BankAccount`.
#   - Initialize attributes `account_number`, `owner_name`, and `balance` in the constructor.
#   - Define a method `display_info` to print the account details.
#
class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def display_info(self):
        print(f"account_number: {self.account_number}")
        print(f"owner_name: {self.owner_name}")
        print(f"balance: {self.balance}")


#2. Define the Subclass (`SavingsAccount`):
#   - Create a subclass `SavingsAccount` that inherits from `BankAccount`.
#   - Initialize additional attribute `interest_rate` in the constructor.
#   - Call the superclass constructor to initialize inherited attributes.
#   - Override the `display_info` method to include the interest rate information.
#
class SavingsAccount(BankAccount):
    #def __int__(self, account_number, owner_name, balance=0,interest_rate=0):
        #super().__init__(account_number, owner_name, balance=0)

    def __init__(self, *args, interest_rate=0, **kwargs):
        super().__init__(*args, **kwargs)
        self.interest_rate = interest_rate

    def display_info(self):
        super().display_info()
        print(f"SA Interest rate:",self.interest_rate)


#3. Create an Instance of `SavingsAccount`:
#   - Instantiate an object of `SavingsAccount` with specific values for `account_number`, `owner_name`, `balance`, and `interest_rate`.
#
savingsaccount_1 = SavingsAccount('Srihari','AC12345',balance=5000,interest_rate=2)

#4. Display Account Information:
#   - Call the `display_info` method on the `SavingsAccount` instance to print all account details, including the interest rate.

savingsaccount_1.display_info()