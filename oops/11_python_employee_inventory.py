# Employee Management System
class EmployeeManagement:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, age, salary):
        self.employees[emp_id] = {"name": name, "age": age, "salary": salary}

    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            return "Employee removed."
        return "Employee not found."

    def display_employees(self):
        return self.employees
    
    def update_employee_salary(self, emp_id, new_salary):
        if emp_id in self.employees:
            self.employees[emp_id]["salary"] = new_salary
            return f"Salary for {self.employees[emp_id]['name']} updated to {new_salary}"
        return "Employee not found."


# Product Inventory Management System
class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product_name, quantity):
        self.products[product_name] = self.products.get(product_name, 0) + quantity

    def update_quantity(self, product_name, quantity):
        if product_name in self.products:
            self.products[product_name] = quantity
            return "Quantity updated."
        return "Product not found."

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
            return "Product removed."
        return "Product not found."

    def display_inventory(self):
        return self.products


# Employee Payroll System
class PayrollSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, monthly_salary):
        self.employees[emp_id] = {"name": name, "monthly_salary": monthly_salary}

    def calculate_salary(self, emp_id):
        if emp_id in self.employees:
            return f"{self.employees[emp_id]['name']} earns {self.employees[emp_id]['monthly_salary']} per month."
        return "Employee not found."

    def display_employees(self):
        return self.employees
