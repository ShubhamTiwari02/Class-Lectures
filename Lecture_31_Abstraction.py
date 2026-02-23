#Abstraction - Hiding the internal details and showing only the functionality to the user. It helps in reducing complexity and allows the user to interact with the system without needing to understand the underlying implementation.
#This helps in reducing complexity and allows the user to interact with the system without needing to understand the underlying implementation. It also helps in improving security by hiding sensitive information from the user.

#2 types of abstraction:
#1. Data Abstraction: It focuses on hiding the internal details of data and only exposing the necessary information to the user. This is achieved through the use of classes and objects in object-oriented programming. For example, a class can have private attributes that are not accessible to the user, and
#2. Procedural/process Abstraction: It focuses on hiding the internal details of a process or a function and only exposing the necessary information to the user. This is achieved through the use of functions and methods in programming. For example, a function can have a complex implementation, but the user only needs to know how to call the function and what parameters it takes.
#A class is said to be abstract class its can not be instantiated and it can have abstract methods which are methods that are declared but not implemented in the abstract class. The implementation of the abstract methods is done in the derived classes that inherit from the abstract class. This allows for a common interface to be defined in the abstract class, while allowing for different implementations in the derived classes.

#we have to import ABC and abstractmethod from the abc module to create an abstract class in Python. The ABC class is used as a base class for defining abstract classes, and the abstractmethod decorator is used to declare methods as abstract methods that must be implemented in the derived classes.
from abc import ABC, abstractmethod
class Demo(ABC):
    @abstractmethod
    def display(self):
        print("This is an abstract method")
    def method1(self):
        print("This is a concrete method")

class Derived(Demo):
    def display(self):
        super().display() # This will call the display method of the abstract class
        return 
        #print("This is the implementation of the abstract method in the derived class")

obj = Derived()
obj.display() # This will call the display method of the derived class which will call the display method of the abstract class
obj.method1() # This will call the concrete method of the abstract class
#obj = Demo() # This will give an error because we cannot instantiate an abstract class
#obj.method1() # This will give an error because we cannot call a method of an abstract class


#Encapsulation - It is the process of wrapping data and methods into a single unit called a class. It helps in hiding the internal details of the class and only exposing the necessary information to the user. This is achieved through the use of access modifiers such as private, protected, and public in object-oriented programming. Encapsulation helps in improving security by preventing unauthorized access to the data and methods of a class. It also helps in improving code maintainability by allowing the internal implementation of a class to be changed without affecting the external code that uses the class.
# class PersonalInfo:
#     def __init__(self, name, age):
#         self.name = name  # public variable
#         self.age = age    # public variable
    
#     def get_name(self):
#         return "My name is " + self.name
    
#     def get_age(self):
#         return "My age is " + str(self.age)
    
# person = PersonalInfo("Alice", 30)
# print(person.get_name())  # Output: My name is Alice
# print(person.get_age())   # Output: My age is 30