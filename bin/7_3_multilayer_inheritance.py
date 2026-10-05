"""
In multilevel inheritance, a subclass inherits from another subclass.
In the bank account example, we'll create a CollegeSavingsAccount class that inherits from the SavingsAccount class.
"""

class BankAccount:
    def __init__(self, account_number: str, owner_name: str, balance: float = 0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Owner Name: {self.owner_name}")
        print(f"Balance: ${self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number: str, owner_name: str, balance: float = 0, interest_rate: float = 0.0):
        super().__init__(account_number, owner_name, balance)
        self.interest_rate = interest_rate

    def display_info(self):
        super().display_info()
        print(f"Interest Rate: {self.interest_rate}%")

class CollegeSavingsAccount(SavingsAccount):
    def __init__(self, account_number: str, owner_name: str, balance: float = 0, interest_rate: float = 0.0, college_savings_rate: float = 0.0):
        super().__init__(account_number, owner_name, balance, interest_rate)
        self.college_savings_rate = college_savings_rate

    def display_info(self):
        super().display_info()
        print(f"College Savings Rate: {self.college_savings_rate}%")

college_acc = CollegeSavingsAccount("345678", "Dilip", 2000, 3.0, 1.0)
college_acc1 = CollegeSavingsAccount("345679", "Arya", 3000, 2.5, 1.5)
college_acc.display_info()
college_acc1.display_info()