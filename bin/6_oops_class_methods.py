# Blueprint/design for any object
#  classs(combination of properties and behaviour)  # modules and variables

#CLASS
class Car:
    def __init__(self, make, model):  # Corrected the spelling
        self.make = make
        self.model = model

    def drive(self):
        print(f"The {self.make} {self.model} is driving.")


class Cake:
    ingredients = ["flour", "sugar", "eggs"]

    def bake(self):
        print("Baking the cake...")

#OBJECT
my_cake = Cake()  # object creation
my_cake.bake()
# Create an instance of the Car class
my_car1 = Car("kia", "sonet")
my_car1.drive()
my_car2 = Car("Toyota", "Innova")
my_car2.drive()
my_car3 = Car("Kia", "Seltos")
my_car3.drive()


# INHERITANCE
class Parent:
    def __init__(self, name):  # instance method
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")


class Child(Parent):
    def __init__(self, name, age):  # instance method
        super().__init__(name)  # super class
        self.age = age

    def display_age(self):
        print(f"I am {self.age} years old")


# Create an instance of Child
child = Child("Dilip", 25)

# Use the inherited greet method
child.greet()  # Output: Hello, I am Alice

# Use the child's own display_age method
child.display_age()  # Output: I am 10 years old


# ABSTRACTION
from abc import ABC, abstractmethod
#from math  import pi

class AbstractShape(ABC):  # Shape is inherited from ABC
    @abstractmethod
    def area(self):
        pass

# Define the Circle class, which inherits from AbstractShape
class AbstractCircle(AbstractShape):   # Circle is inherited from AbstractShape
    def __init__(self, radius):  # Ensure the __init__ method takes a radius parameter
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


# Define the Rectangle class, which inherits from AbstractShape
class AbstractRectangle(AbstractShape):  # Rectangle is inherited from AbstractShape
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Create instances
circle = AbstractCircle(5)  # Instance/Method
rectangle = AbstractRectangle(4, 6)

# Use the area method from each instance
print("Circle area:", circle.area())  # Output: Circle area: 78.53975
print("Rectangle area:", rectangle.area())  # Output: Rectangle area: 24


# POLYMORPHISM
class Shape:
    def area(self):
        pass

class PolyCircle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class PolyRectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Demonstrate polymorphism
def print_area(shape):
    print(f"The area of the shape is: {shape.area()}")


# Create instances
poly_circle = PolyCircle(5)
poly_rectangle = PolyRectangle(4, 6)

# Use polymorphism to calculate and print areas
print_area(poly_circle)  # camera  # 78.53975
print_area(poly_rectangle)  # app booking # 24

# ENCAPSULATION
class EncapsulatedCircle:
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.14159 * self.__radius ** 2


class EncapsulatedRectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height


# Create instances
enc_circle = EncapsulatedCircle(5)
enc_rectangle = EncapsulatedRectangle(4, 6)

print("Circle area:", enc_circle.area())
print("Rectangle area:", enc_rectangle.area())