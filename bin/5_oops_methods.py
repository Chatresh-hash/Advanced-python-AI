"""
Calculating Interest for an Account, Calculating Account Balance after Deposit & Withdrawal
"""

#Step 1: Initialize Account Attributes
#Define the account balance.
#
#Define the account interest rate.
#
#Step 2: Deposit Amount
#Accept the deposit amount as input.
#
#Increase the account balance by the deposit amount.
#
#Step 3: Withdraw Amount
#Accept the withdrawal amount as input.
#
#Check if the account balance is sufficient for the withdrawal.
#
#If funds are sufficient, decrease the account balance by the withdrawal amount.
#
#If funds are insufficient, print an error message indicating insufficient funds.
#
#Step 4: Calculate Interest
#Multiply the account balance by the interest rate to calculate the interest.
#
#Step 5: Return Results
#Return or print the calculated interest.
#
#Return or print the updated balance

"""
Change Interest for All Accounts at Bank Level, 
Setting and Getting the Bank's Interest Rate, Updating Interest Rates for All Accounts
"""

#1. **Initialize Bank Class:**
#    - The class `Bank` is created.
#    - The class has two class variables: `interest_rate` set to `0.05` and `accounts` initialized as an empty list.
#
class Bank:
    interest_date = 0.5  # class variable
    accounts = []

#2. **Define Class Methods:**
#    - `set_interest_rate(cls, rate)`: This method sets the class variable `interest_rate` to a new value.
#    - `get_interest_rate(cls)`: This method returns the current `interest_rate` of the class.
#    - `create_account(cls, account_number, account_holder)`: This method creates a new account with the given `account_number` and `account_holder`, sets its initial `balance` to `0.0`, adds it to the `accounts` list, and returns the created account.
#    - `get_account(cls, account_number)`: This method searches for an account by `account_number` in the `accounts` list and returns the account if found, otherwise returns `None`.

    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_date = rate

# 3. **Set and Get Interest Rate: **
#    - Call `Bank.set_interest_rate(0.06)` to change the interest rate to `0.06`.
#    - Call `Bank.get_interest_rate()` to get the updated interest rate and print it.
#
    @classmethod
    def get_interest_rate(cls):
        return cls.interest_date


#4. **Create Bank Accounts:**
#    - Call `Bank.create_account('001', 'Dilip')` to create an account for Dileep with account number '001'.
#    - Call `Bank.create_account('002', 'Anil')` to create an account for Anil with account number '002'.

    @classmethod
    def create_account(cls,account_number,account_holder):
        account = {"account_number" : account_number,
                   "account_holder": account_holder,
                   "balance" : 0}

        cls.accounts.append(account)
        return account



#5. **Get Account Information:**
#    - Call `Bank.get_account('001')` to get Dilip's account information and store it in `Dileep_account`.
#    - Call `Bank.get_account('002')` to get Anil's account information and store it in `Anil_account`.

    @classmethod
    def get_account(cls,account_number):
        for account in cls.accounts:
            if account['account_number'] == account_number:
                return account
        return None


#6. **Print Account Information: **
#    - Print Dilip's account information.


Bank.set_interest_rate(0.6)

print("Updated Bank interest:",Bank.get_interest_rate())

#    - Print Anil's account information.

Bank.create_account('AC001','Sreehari')

Bank_account_1 = Bank.get_account('AC001')


print("Bank_account_1:",Bank_account_1)

"""
Validate Account Number, Converting Currency, Calculating Loan Eligibility, Calculating Mortgage Payments
"""

#Step 1: Validate Account Number
#Define a static method.
#

class Utility:
    @staticmethod
#Check if the account number valid or not.
    def validate_account_number(account_number):
        return len(account_number) == 10 and account_number.isalnum()


#Step 2: Convert Currency
#Define a static method.
    @staticmethod
    def convert_currency(amount,source_currency, target_currency):
        exchange_rates = {
            ('USD','EUR'): 0.8,
            ('USD','INR') : 80.1,
            ('EUR','INR'): 95.0,
            ('INR', 'USD'): 1.1
        }
        return  str(amount * exchange_rates[(source_currency,target_currency)]) +  ' ' + target_currency

#Use predefined exchange rates to convert currency.
#
#Step 3: Calculate Loan Eligibility
#Define a static method.
#
#Check if the user's income and credit score meet the eligibility criteria.
#
#Step 4: Calculate Mortgage Payments
#Define a static method.
#
#Calculate mortgage payments based on principal, interest rate, and term

is_valid = Utility.validate_account_number("ACC1223300")
print("is_valid:",is_valid)
if is_valid:
    print("Valid Account_number")
else:
    print("Not a Valid Account_number")



converted_amount  = Utility.convert_currency(100,'USD','INR')
print("converted_amount:",converted_amount)

"""
Different Types of Accounts Calculating Interest, Implementing Different Types of Loans
"""
#
#Step 1: Define Abstract Base Class
#Import Modules: Import ABC and abstractmethod from the abc module.
#
#Define Abstract Class: Create an abstract class named Account with an abstract method calculate_interest.
#
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    @abstractmethod
    def calculate_interest(self) -> float:
        pass

    def get_balance(self):
        return self.balance


#Step 2: Subclass for Different Account Types
#Define Subclasses: Create subclasses for different account types (SavingsAccount, CheckingAccount, FixedDepositAccount).
#

#Implement Abstract Method: Implement the calculate_interest method in each subclass with specific interest rate calculations.
#
class Savingsaccount(Account):
    #def __init__(self, account_number, account_holder, balance=0):
        #super().__init__(account_number, account_holder, balance)
    def calculate_interest(self):
        interest_rate = 0.5
        return self.balance * interest_rate

SA = Savingsaccount('SA123', 'Sreehari', 10000)
print("SA account interest:", SA.calculate_interest())






#Step 3: Implement Different Loan Types
#Define Abstract Loan Class: Create an abstract class named Loan with an abstract method calculate_payment.
#
#Define Loan Subclasses: Create subclasses for different loan types (HomeLoan, AutoLoan).
#
#Implement Abstract Method: Implement the calculate_payment method in each subclass with specific payment calculations.