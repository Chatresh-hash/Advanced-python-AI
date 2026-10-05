"""
Abstraction :
Abstraction in Python involves hiding the complex implementation details of a class and only exposing the necessary
features to the outside world.
This simplifies the usage of the class and makes the code more maintainable and scalable.

"""
from abc import abstractmethod


class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    @abstractmethod
    def calculate_interest(self) -> float:
        pass

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def calculate_interest(self) -> float:
        interest_rate = 0.2
        return self.balance * interest_rate


class CurrentAccount(BankAccount):
    def calculate_interest(self) -> float:
        interest_rate = 0.5
        return self.balance * interest_rate


class CollegeAccount(BankAccount):
    def calculate_interest(self) -> float:
        interest_rate = 0.9
        return self.balance * interest_rate

savings_account = SavingsAccount('SA123','Srihari',1000)
current_account = CurrentAccount('SA123','Srihari',1000)
college_account = CollegeAccount('SA123','Srihari',1000)

print("savings_account cal int :",savings_account.calculate_interest())
print("current_account cal int :",current_account.calculate_interest())
print("college_account cal int :",college_account.calculate_interest())