"""
class : Inheritance
In a new class, we are extending functionality of existing class
"""

'''
Instead of altering Employee class, extend and add below methods in new class
1) add_tax
2) view_tax
3) update view_salary to return sal-tax
'''

class Employee:
    company_name = "XYZ Company"
    def add_name(self, n):
        self.name =n
    def add_salary(self, s):
        self.salary = s
    def view_name(self):
        return self.name
    def view_salary(self):
        return self.salary
    @classmethod
    def add_ceo_name(cls, n):
        cls.ceo_name = n
    @classmethod
    def view_ceo_name(cls):
        return cls.ceo_name
    @staticmethod
    def compute_avg_salary(sal1, sal2):
        return (sal1+sal2)/2



class NewEmployeeClass(Employee): # 1) Employee - super/parent class 2) NewEmployeeClass - sub/child class
    def add_tax(self, t):
        self.tax = t
    def view_tax(self):
        return self.tax
    # POLYMORPHISM : allowed to use same name as super class
    def view_salary(self): # When we call method, this will OVERRIDE(TAKES pririoty) super class method
        return self.salary - self.tax

# Requirement : store 2 employees details like name, salary, company name and
# PRINT 2 employee details


# We need 2 objects to store 2 employee details
Employee1 = NewEmployeeClass()
Employee2 = NewEmployeeClass()

Employee1.add_name("emp-1")
Employee1.add_salary(20000)
Employee1.add_tax(2000)

Employee2.add_name("emp-2")
Employee2.add_salary(22000)
Employee2.add_tax(2200)

print("Employee 1 Name : ", Employee1.view_name())
print("Employee 1 Salary : ", Employee1.view_salary())
print("Employee 1 tax : ", Employee1.view_tax())
print("Employee 1 Company Name : ", NewEmployeeClass.company_name)

print("Employee 2 Name : ", Employee2.view_name())
print("Employee 2 Salary : ", Employee2.view_salary())
print("Employee 2 tax : ", Employee2.view_tax())
print("Employee 2 Company Name : ", NewEmployeeClass.company_name)


NewEmployeeClass.add_ceo_name('CEO-1')
print("CEO Name : ", NewEmployeeClass.view_ceo_name())

s1 = Employee1.view_salary()
s2 = Employee2.view_salary()
avg_sal = NewEmployeeClass.compute_avg_salary(s1, s2)
print("avg_sal : ", avg_sal)