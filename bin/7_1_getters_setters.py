"""
Class: Class Objects and Variables with getters and setters

"""
#1. **Define the Base Class (`BankAccount`):**
#   - Create a class `BankAccount`.
class BankAccount:
    #   - Initialize attributes `_account_number`, `_owner_name`, and `_balance` in the constructor using protected access (underscore prefix).
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    #   - Define getter methods:
    #     - `get_account_number`: Returns the account number.
    #@property
    def get_account_number(self):
        return self.account_number

    #     - `get_owner_name`: Returns the owner's name.
    #@property
    def get_owner_name(self):
        return self.owner_name

    #     - `get_balance`: Returns the balance.
    #@property
    def get_balance(self):
        return self.balance

    #   - Define a setter method `set_balance` to update the balance:
    #@set_balance.setter
    def set_balance(self, new_balance):
        #     - Check if the new_balance is non-negative.
        if new_balance >= 0:
            #     - If valid, update the balance.
            self.balance = new_balance
        #     - If invalid, print an error message.
        else:
            print("Error: Balance is negative")

    #   - Define a method `deposit` to add an amount to the balance:
    #     - Check if the amount is positive.
    #     - If valid, update the balance and print the new balance.
    #     - If invalid, print an error message.
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("balance:", self.balance )
        else:
            print("Error: Deposit amount must be positive")

    #   - Define a method `withdraw` to subtract an amount from the balance:
    #     - Check if the amount is positive and less than or equal to the current balance.
    #     - If valid, update the balance and print the new balance.
    #     - If invalid, print an error message.

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw amount: {amount}")
            print(f"Balance amount: {self.balance}")
        else:
            print("Error: Insufficient Balance")


#2. **Create an Instance of `BankAccount`:**
#   - Instantiate an object of `BankAccount` with specific values for `account_number`, `owner_name`, and `balance`.
Bankaccount1 = BankAccount('BA123456', 'Sreehari', 500)
Bankaccount2 = BankAccount('BA123457', 'Anil', 500)

#3. **Get Account Information Using Getter Methods:**
#   - Call the getter methods `get_account_number`,
#   `get_owner_name`, and `get_balance` to retrieve the account information.
#   - Print the account information.
print("get_account_number:", Bankaccount1.get_account_number())
print("get_owner_name:", Bankaccount1.get_owner_name())
print("get_balance:", Bankaccount1.get_balance())

#4. **Perform Deposit and Withdraw Operations:**
#   - Call the `deposit` method to add an amount to the balance.
#   - Call the `withdraw` method to subtract an amount from the balance.
Bankaccount1.deposit(10000)
Bankaccount1.withdraw(5000)

#5. **Attempt to Set Negative Balance Using Setter Method:**
#   - Call the setter method `set_balance` with a negative balance.
#   - Print an error message if the balance is invalid.
Bankaccount1.set_balance(20000)
print("Get_balance:",Bankaccount1.get_balance())