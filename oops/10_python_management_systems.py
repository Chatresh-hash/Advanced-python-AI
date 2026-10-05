from importlib import import_module

BankAccount = import_module("9_python_basic_classes").BankAccount

# Bank Management System    
class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, balance=0):
        self.accounts[account_number] = BankAccount(account_number, balance)

    def deposit(self, account_number, amount):
        return self.accounts[account_number].deposit(amount)

    def withdraw(self, account_number, amount):
        return self.accounts[account_number].withdraw(amount)

    def check_balance(self, account_number):
        return f"Balance: {self.accounts[account_number].balance}"


# Library Management System
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def lend_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return f"{book} has been lent."
        return "Book not available."

    def return_book(self, book):
        self.books.append(book)
        return f"{book} has been returned."

    def display_books(self):
        return f"Available Books: {', '.join(self.books)}"
