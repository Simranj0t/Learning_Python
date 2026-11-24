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

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):  # Overriding the parent method
        return f"{self.name} says Woof!"

dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy says Woof!
 """