class BankAccount:
    def __init__(self,account_number,holder_name,balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    # Method Overloading using *args (variable arguments)
    def withdraw(self, *args):   # *agrs (a1,a2,a3........)
        if len(args) == 1:
            # Withdraw by amount only
            amount = args[0]
            self.withdraw_amount(amount)
        elif len(args) == 2 and isinstance(args[1], str):  # True
            # Withdraw with amount and currency
            amount, currency = args
            self.withdraw_amount(amount)
            print(f"Currency: {currency}")
        elif len(args) == 3:
            # Withdraw with amount, currency, and name
            amount, currency, name = args
            if name == self.holder_name:
                self.withdraw_amount(amount)
                print(f"Currency: {currency}, Holder Name Verified: {name}")
            else:
                print("Holder name does not match.")
        else:
            print("Invalid withdrawal request.")

    def withdraw_amount(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient balance")

    def display(self):
        print(f"Account Holder: {self.holder_name}, Account Number: {self.account_number}, Balance: {self.balance}")

# Example Usage
account1 = BankAccount(1234,"Dilip",5000)
account2 = BankAccount(5678,"John",3000)

# Overloaded withdraw calls
account1.withdraw(500)  # Withdraw by amount only  # arg1
account1.withdraw(800, "USD")  # Withdraw with amount and currency  # arg1, agr2
account1.withdraw(1000, "EUR", "Dilip")  # Withdraw with amount, currency, and holder name verification
# Incorrect holder name, withdrawal denied
account2.withdraw(500, "USD", "Jane")  # Incorrect holder name, withdrawal denied
account2.withdraw(2000, "USD", "John")  # Withdraw with amount, currency, and holder name verification
account2.withdraw(4000)  # Insufficient balance
