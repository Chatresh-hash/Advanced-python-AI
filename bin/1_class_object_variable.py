"""
Class: Class Objects and Class Variables
"""

# -----------------
# CLASS OBJECTS: 1) Company, 2) Employee1, 3) Employee2
# CLASS VARIABLES: 1) name, salary in Employee class, 2) name inside Company class
# ------------------

class Company:
    # Class variable
    name = "TechCorp"

    def __init__(self, location):
        # Instance variable
        self.location = location


class Employee:
    # Class variables
    company_name = Company.name
    base_salary = 50000

    def __init__(self, name, salary=None):
        # Instance variables
        self.name = name
        self.salary = salary if salary else Employee.base_salary


# Create class objects
company = Company("Hyderabad")
employee1 = Employee("Alice", 60000)
employee2 = Employee("Bob")  # Will use default base_salary

# Print details
print("Course_id:", 1001, type(1001))
print("Company Name:", Company.name)
print("Company Location:", company.location)

print("Employee1:", employee1.name, "| Salary:", employee1.salary, "| Company:", employee1.company_name)
print("Employee2:", employee2.name, "| Salary:", employee2.salary, "| Company:", employee2.company_name)
