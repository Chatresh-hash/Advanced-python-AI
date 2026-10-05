# Creating the class using Instance method
# AT student we have changed the grade of each student: Instance method
class Student:
    def __init__(self, name, grade):
        # Instance variables for each student's name and grade
        self.name = name
        self.grade = grade

    def change_grade(self, new_grade):
        # Method to change the grade of this specific student
        self.grade = new_grade

# Instance 1 that is student-1
student1 = Student("Dilip", 'B')  # Creating an instance of the Student class for Alice
student1.change_grade('A')
print(f"{student1.name}'s New grade: {student1.grade}")  # Output: Dilip's original grade:

#Instance 2 that is student-2
student2 = Student("Varun", 'C')  # Creating an instance of the Student class for Alice
student2.change_grade('A')
print(f"{student2.name}'s New grade: {student2.grade}")  # Output: Varun's original grade:

##########################################################################################
# Creating the class using Instance method
class SchoolInstance:
    def __init__(self):
        self.grading_policy = "A: 90-100, B: 80-89, C: 70-79, D:60-69, E: 40-59, F:0-39"

    def change_grading_policy(self, new_policy):
        self.grading_policy = new_policy

# Usage
# Instance 1 that is student-1 for grading_policy change
std1 = SchoolInstance()
std1.change_grading_policy("A: 90-100, B: 80-89, C: 70-79, D:60-69, E: 35-59, F:0-34")
print(std1.grading_policy)  # A: 90-100, B: 80-89, C: 70-79, D:60-69, E: 35-59, F:0-34

std2 = SchoolInstance()
std2.change_grading_policy("A: 80-100, B: 70-89, C: 60-79, D:50-69, E: 35-49, F:0-34")
print(std2.grading_policy)  #  80-100, B: 70-89, C: 60-79, D:50-69, E: 35-49, F:0-34

####################################################################################
# Creating the class using Instance method
class BankAccount:
    def __init__(self, owner, balance=0):
        # Instance variables for each account's owner and balance
        self.owner = owner
        self.balance = balance

    # Instance method to deposit money into the account
    def deposit(self, amount):
        self.balance += amount
        #2000
        return f"{amount} deposited. New balance: {self.balance}"

    # Instance method to withdraw money from the account
    def withdraw(self, amount):
        if amount > self.balance:
            #500 > 2000
            return "Insufficient funds"
        self.balance = self.balance - amount
        return f"{amount} withdrawn. New balance: {self.balance}"

# Instance 1 that is account-1
account1 = BankAccount(owner='Dilip',balance=1000) # Creating an instance of BankAccount for Dilip
print(account1.deposit(1000))  # Output: 1000 deposited. New balance: 2000
print(account1.withdraw(500))  # Output: 300 withdrawn. New balance: 1500

# Instance 2 that is account-2
account2 = BankAccount(owner='varun',balance=2000) # Creating an instance of BankAccount for Dilip
print(account2.deposit(1000))  # Output: 1000 deposited. New balance: 2000
print(account2.withdraw(500))  # Output: 300 withdrawn. New balance: 1500
##################################################################################################

# Creating the class using Class method

class SchoolClassMethod:
    # Class variable
    grading_policy = "A: 90-100, B: 80-89, C: 70-79, D:60-69 , E: 40-59 , F:0-39"  # existing_policy

    @classmethod
    def change_grade_policy(cls,new_policy):  # cls paramter means at school level grading_policy change
        cls.grading_policy = new_policy

# Usage
SchoolClassMethod.change_grade_policy("A: 90-100, B: 80-89, C: 70-79, D:60-69 , E: 35-59 , F:0-34")
print(SchoolClassMethod.grading_policy)

##################################################################################################

# Creating the class using Class method

class BankAccountInterest:
    # Class attribute shared by all accounts (initial interest rate)
    interest_rate = 0.05

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # Class method to update the interest rate for all accounts
    @classmethod
    def set_interest_rate(cls,new_rate):
        cls.interest_rate = new_rate

# Usage
print(BankAccountInterest.interest_rate)  # Output: 0.05

# Change interest rate for all accounts
BankAccountInterest.set_interest_rate(0.5)
print(BankAccountInterest.interest_rate)  # Output: 0.5


##################################################################################################

# Creating the class using static method
class School:
    grading_policy = "A: 90-100, B: 80-89, C: 70-79, D:60-69, E: 40-59, F:0-39"

    @staticmethod
    def is_valid_grade(grade):
        # This static method checks if a given grade is within the valid range (0-100)
        return 'A'<= grade <= 'F'   # true:  A-F values  and false : other values


# Usage
print(School.is_valid_grade('A'))  # Output: True (A-F is within the valid range)
print(School.is_valid_grade('H')) # Output: False (H is not within the valid range)
#########################################################################################
# Creating the class using static method
class BankAccountValidator:
    def __int(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    # Static method to check if a provided account number is valid
    @staticmethod
    def validate_account_number(account_number):
        # Simple check to ensure account number is 10 digits long
        return len(str(account_number)) == 10

# Usage
print(BankAccountValidator.validate_account_number(8884510006))  # Output: True
print(BankAccountValidator.validate_account_number(123456666))  # Output: False
#####################################################################################
# Creating the class using abstract method

from abc import ABC, abstractmethod
#Main Class
class SchoolBase(ABC):  # parent class
    grading_policy = "A: 90-100, B: 80-89, C: 70-79, D:60-69, E: 40-59, F:0-39"

    @abstractmethod
    def change_grading_policy(self,new_policy):
        pass

#Sub Class
class SchoolPolicy(SchoolBase):  # child class
    def change_grading_policy(self,new_policy):
        SchoolPolicy.grading_policy= new_policy


# Usage
school = SchoolPolicy()
school.change_grading_policy("A: 90-100, B: 80-89, C: 70-79, D:60-69, E: 35-59, F:0-34")
print(school.grading_policy)  # A: 90-100, B: 80-89, C: 70-79, D:60-69, E: 35-59, F:0-34

#############################################################################################
# Creating the class using abstract method

class BankAccountBase(ABC):
    # Abstract method to be implemented by subclasses
    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccountBase):
    def __init__(self, balance):
        self.balance = balance

    # Implement the abstract method
    def calculate_interest(self):
        return self.balance * 0.04  # 4% interest for savings account

class CheckingAccount(BankAccountBase):
    def __init__(self, balance):
        self.balance = balance

    # Implement the abstract method
    def calculate_interest(self):
        return self.balance * 0.02  # 2% interest for checking account

# Usage
savings = SavingsAccount(2000)
checking = CheckingAccount(1000)

print(savings.calculate_interest())  # Output: 40.0 (4% interest on 1000)
print(checking.calculate_interest())  # Output: 20.0 (2% interest on 1000)