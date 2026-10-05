"""
Class : Operators

In python for each operator there is name given,
example:
__add__ name is given to +
__sub__ name is given to -
__mul__ name is given to *

Now, if we want to support any operator then
respective method should be implemented in our class
"""

class Employee:
    def __init__(self, name):
        self.name = name
    def __add__(self, other): # __add__(e1, e2) # self=e1, other=e2
        # return 0 # here add of 2 emplouyee object is 0
        # return "Hello" # here add of 2 emplouyee object is 'Hello'
        return e1.name + other.name

e1 = Employee('Dilip')
e2 =Employee('Arya')

result = e1 + e2
print("result : ", result)


class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)  # Returning class

    def __sub__(self, other):
        return Money(self.amount - other.amount)  # Returning class

# Create two Money objects with the same currency
m1 = Money(70)
m2 = Money(40)

# Add the two amounts using the overloaded + operator
m3 = m2 + m1
print(m3.amount)

m4 = m1 - m2
print(m4.amount)

# ------------------
# Traceback (most recent call last):
#   File "C:\python_training\bin\36_class_operator_overloading.py", line 12, in <module>
#     result = e1 + e2
# TypeError: unsupported operand type(s) for +: 'Employee' and 'Employee'
# ------------------