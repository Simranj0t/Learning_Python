# oops has 4 pillars
"""Inheritence - Inheritance in Python is a core object-oriented programming (OOP) concept that allows a new class 
(called a child or derived class) to acquire the attributes and methods of an existing class (called a parent or base class).
 It models an "is-a" relationship (for example, a Dog is an Animal), which promotes code reuse and eliminates duplication
 
 # Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"

# Child Class: Dog
class Dog(Animal):
    def __init__(self, name, breed):
        # Calls constructor based on MRO
        super().__init__(name)  
        self.breed = breed

    def details(self):
        print(self.name, "is a", self.breed)

d = Dog("Buddy", "Golden Retriever")
d.info()      # Parent method
d.details()   # Child method 

Encapsulation in Python is an object-oriented programming concept that bundles data (attributes) and the methods that operate
on that data into a single unit (a class), while restricting direct access to some of an object's internal components.
It helps protect data integrity, prevent accidental changes, and expose only a controlled interface.

class Employee:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def get_salary(self):    # Getter method
        return self.__salary

    def set_salary(self, amount):   # Setter method
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount!")

emp = Employee()
print(emp.get_salary())  # Access salary using getter

emp.set_salary(60000)   # Update salary using setter
print(emp.get_salary())
 
  is a core object-oriented programming (OOP) concept where a single function, operator, or method name can work with 
  different types of objects and behave appropriately for each. The word comes from Greek, meaning "many forms".
 
 class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Car:
    def speak(self):
        return "Honk!"

# All three unrelated objects respond to the same method call
animals_and_objects = [Dog(), Cat(), Car()]

for item in animals_and_objects:
    print(item.speak())

# Output:
# Woof!
# Meow!
# Honk!
 """