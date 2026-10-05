"""
Class : Instance Objects and Instance Variables

Using one class, we can create multiple objects
"""

# Define the Employee Class: Create a class named Employee.
#Define a class variable company_name and set it to "TechCorp".

class Employee:
    company_name = "Onmobile"
    def __init__(self,name, sal):
        self.name = name
        self.sal = sal


# Requirement: store 2 employees details like name, salary, company name and
# PRINT 2 employee details

# We need to Create Employee Objects to store 2 employee details
#Create an object of the Employee class named employee1 with the name "Alice"
# and salary 50,000.

Employee1 = Employee('emp-1',20000)

#Create another object of the Employee class named employee2 with the name "Bob"
# and salary 60,000.

Employee2 = Employee('emp-2', 20000)

#Print Employee Details
# For employee1, print their name, salary, and the company_name.

print("Employee 1 Name",Employee1.name)
print("Employee 1 Salary",Employee1.sal)
print("Employee 1 company_name",Employee1.company_name)
# For employee2, print their name, salary, and the company_name.

print("Employee 2 Name",Employee2.name)
print("Employee 2 Salary",Employee2.sal)
print("Employee 2 company_name",Employee2.company_name)
# ---------------------------
# CLASS/OBJECT COMPLETE PROCESS
# ---------------------------
# POINT - 1 : How object is getting created??
# ---------------------------
# - There is a predefined class 'object'
# - This class acts as the base class for all other classes.
# - Inside 'object' class, there are many methods, in that 2 methods are
#   1) __new__ # Responsible for creating or constructing the object.
#                It is called before the __init__ method.
#   2) __init__ # Responsible for initializing the object with some initial data, if provided.

# Object Creation Process:
# - When an object of a custom class is created,
#   the __new__ method of the object class is internally called to create the object.
#   The __init__ method is then called to initialize the object with any provided data.
#
# - In OOP terminology, all our classes, which we are creating by default inheriting from
#   'object' class. Because of this, our classes, which we are creating, are able
#   to access methods/variables present in 'object' class
# ---------------------------



# ---------------------------
# POINT - 2 : Method Overriding & self
# ---------------------------
# - We can rewrite methods present in 'object' (super class)
# - We wrote __init__ method,
#
# - Now, when we create object like,
#
#   Employee1 = Employee('emp-1', 20000)
#   internally
#   1) Employee1 = Employee.__new__()
#   2) Employee.__init__(Employee1, 'emp-1', 20000)
#       self refers to Employee1
#       Employee1.name="emp-1"
#       Employee1.salary=20000
#
#   Employee2 = Employee('emp-2', 22000)
#   internally
#   1) Employee2 = Employee.__new__()
#   2) Employee.__init__(Employee2, 'emp-2', 22000)
#       self refers to Employee2
#       Employee2.name="emp-2"
#       Employee2.salary=22000
# self : self is to hold current object
#        It allows access to the object's attributes and methods from within the class.
# ---------------------------

# ---------------------------
# POINT - 3
# ---------------------------
# - Totally we have 3 objects 1) Employee 2) Employee1 3) Employee2
# - CLASS OBJECT : 1) Employee
# - CLASS VARIABLE : company_name
# - INSTANCE OBJECTS : 1) Employee1 2) Employee2
# - INSTANCE VARIABLES : 1) name 2) salary
# ---------------------------

# POINT - 4
# ---------------------------
# - Data stored in CLASS OBJECT can be accessed using INSTANCE OBJECTS
print("Access company_name using CLASS OBJECT Employee : ",Employee.company_name )
print("Access company_name using INSTANCE OBJECT Employee1 : ",Employee1.name )
print("Access company_name using INSTANCE OBJECT Employee2 : ",Employee2.name )
# ---------------------------

# ---------------------------
# POINT - 5
# ---------------------------
# - We can say, CLASS OBJECT is common space/place for all INSTANCE OBJECTS
# - We can make use CLASS OBJECT to store data which is common for all INSTANCE OBJECTS
# - Since company_name is common for all INSTANCE OBJECTS/employees, so we stored in
#   CLASS OBJECT
# ---------------------------

print("Employee class:",dir(Employee))