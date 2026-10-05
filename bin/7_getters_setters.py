# getters and setters are used to access and modify
# the private attributes of a class. They provide a way to control the access and modification of these attributes, allowing for validation and encapsulation.

# Banking example
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private attribute for account number
        self.__balance = balance  # private attribute for balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount. Please enter a positive value less than or equal to the balance.")
    
    # Getter for account number
    def get_account_number(self):
        return self.__account_number

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Setter for balance
    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Invalid balance. Please enter a positive value.")
            
# Example usage
account1 = BankAccount("123456789", 1000)
account1.deposit(1000)
account1.deposit(500)  # Invalid deposit
account1.withdraw(200)
account1.withdraw(1000)  # Invalid withdrawal

print(account1.get_balance())
print("Updating balance using setter...")
account1.set_balance(5000)
print(account1.get_balance())