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
"""