"""
Calculating Account Balance after Deposit & Withdrawal
"""


#1. **Define the `BankAccount` Class**
#   - Create a class named `BankAccount`.
class  BankAccount:
#2. **Define the `__init__` Method**
#   - Create an initializer method called `__init__`.
#   - This method will take `account_holder_name` and `balance` as parameters.
#   - Set `self.account_holder_name` to `account_holder_name`.
#   - Set `self.balance` to `balance`, with a default value of 0.
    def __init__(self , account_holder_name, balance=0):
        self.account_holder_name = account_holder_name
        self.balance = balance

#3. **Define the `deposit` Method**
#   - Create a method named `deposit`.
#   - This method will take `amount` as a parameter.
#   - Add `amount` to `self.balance`.
#   - Print a message showing the deposited amount and the new balance.
    def deposit(self, amount):
        if amount > 0:
            self.balance  = self.balance + amount
        else:
            print("Please enter positive value for balance")

#4. **Define the `withdraw` Method**
#   - Create a method named `withdraw`.
#   - This method will take `amount` as a parameter.
#   - Check if `amount` is greater than `self.balance`.
#     - If true, print "Insufficient funds".
#     - If false, subtract `amount` from `self.balance` and print a message showing the withdrawn amount and the new balance.

    def withdraw(self,amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance  = self.balance - amount
            else:
                print("Insufficient Funds")
        else:
            print("Please enter positive value for withdraw")


#5. **Define the `check_balance` Method**
#   - Create a method named `check_balance`.
#   - Print the current balance (`self.balance`).
    def check_balance(self):
        print(f"The available balance for your account: {self.balance}")




#6. **Create a `BankAccount` Object**
#   - Create an instance of the `BankAccount` class named `account1`.
#   - Initialize `account1` with the name "John Doe" and a balance of 1000.

account_1 = BankAccount("Sreehari",50000)
account_2 = BankAccount("Anil",70000)
account_3 = BankAccount("Sandeep",90000)
account_4 = BankAccount("Kalyani",100000)
#7. **Deposit Money into the Account**
#   - Call the `deposit` method on `account1` with an amount of 500.

account_1.deposit(50000)
account_2.deposit(60000)
account_3.deposit(70000)
account_4.deposit(40000)
#8. **Withdraw Money from the Account**
#   - Call the `withdraw` method on `account1` with an amount of 200.

account_1.withdraw(120000)
account_2.withdraw(50000)
account_3.withdraw(35000)
account_4.withdraw(90000)
#9. **Check the Account Balance**
#   - Call the `check_balance` method on `account1` to print the current balance.

account_1.check_balance()
account_2.check_balance()
account_3.check_balance()
account_4.check_balance()


