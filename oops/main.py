
import importlib.util
import sys
from pathlib import Path


def load_module(module_name: str, file_name: str):
    file_path = Path(__file__).resolve().parent / file_name
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module '{module_name}' from '{file_path}'")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


basic_classes = load_module("basic_classes", "9_python_basic_classes.py")
management_systems = load_module("management_systems", "10_python_management_systems.py")
employee_inventory = load_module("employee_inventory", "11_python_employee_inventory.py")

Rectangle = basic_classes.Rectangle
Employee = basic_classes.Employee
BankAccount = basic_classes.BankAccount
BankSystem = management_systems.BankSystem
Library = management_systems.Library
EmployeeManagement = employee_inventory.EmployeeManagement
Inventory = employee_inventory.Inventory
PayrollSystem = employee_inventory.PayrollSystem

# Rectangle
rect = Rectangle(15, 5)
print("Rectangle Area:", rect.area())
print("Rectangle Perimeter:", rect.perimeter())

# Employee
emp = Employee("Alice", 30, 50000)
print(emp.display_details())
emp.update_salary(55000)
print(emp.display_details())

# BankAccount
bank_acc = BankAccount("12345", 1000)
bank_acc2 = BankAccount("12346", 1000)

print(bank_acc.deposit(500))
print(bank_acc.withdraw(300))
print(bank_acc2.deposit(1000))
print(bank_acc2.withdraw(500))

# Bank System
bank = BankSystem()
bank.create_account("111", 2000)
print(bank.deposit("111", 500))
print(bank.check_balance("111"))

# Library
lib = Library()
lib.add_book("Python Basics")
lib.add_book("Data Structures")
print(lib.display_books())
print(lib.lend_book("Python Basics"))
print(lib.display_books())

# Employee Management
emp_mgmt = EmployeeManagement()
emp_mgmt.add_employee("E01", "Bob", 28, 40000)
emp_mgmt.add_employee("E02", "Charlie", 32, 45000)
emp_mgmt.update_employee_salary("E01", 42000)
emp_mgmt.update_employee_salary("E02", 47000)   
print(emp_mgmt.display_employees())

# Inventory
inv = Inventory()
inv.add_product("Laptop", 10)
inv.update_quantity("Laptop", 15)
print(inv.display_inventory())

# Payroll
payroll = PayrollSystem()
payroll.add_employee("E01", "Bob", 40000)
print(payroll.calculate_salary("E01"))
