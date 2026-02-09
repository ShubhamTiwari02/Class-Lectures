#Inheritance - A class can inherit attributes and methods from another class.

#1. Single Inheritance
# class Parent:
#     def greet(self):
#         return "Hello from Parent"
#     def greet1(self):
#         return "Good morning from Parent"
#     def greet2(self):
#         return "Good night from Parent"
    
# class Child(Parent):
#     def greet_child(self):
#         return "Hello from Child"
    
# c1 = Child()
# print(c1.greet_child())   
# print(c1.greet())   
# print(c1.greet1())   
# print(c1.greet2())

# class Parent:
#     def parent_method(Yashika, name = "Akash", age = 400):
#         Yashika.name = name
#         Yashika.age = age
#         return "This is a method in the Parent class. Name: {}, Age: {}".format(name, age)
    
# class Child(Parent):
#     def child_method(Yashika, name = "Akash", age = 300):
#         Yashika.name = name
#         Yashika.age = age
#         return "This is a method in the Child class. Name: {}, Age: {}".format(name, age)

# c1 = Child()
# p1 = Parent()
# print(c1.parent_method())
# print(p1.child_method())

#2. Multiple Inheritance
# class Parent1:
#     def method1(self):
#         return "This is method 1 from Parent1"
    
# class Parent2:
#     def method2(self):
#         return "This is method 2 from Parent2"
    
# class Parent3:
#     def method1(self):
#         return "This is method 3 from Parent3"

# class Child(Parent1, Parent2, Parent3):
#     def child_method(self):
#         return "This is a method in the Child class"  

# #MRO - Method Resolution Order - The order in which Python looks for a method in a hierarchy of classes.

# c1 = Child()
# print(c1.method1())
# print(c1.method2())   
# print(c1.method1())
# print(c1.child_method())


# class Division:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
    
#     def divide(self):
#         if self.b != 0:
#             return self.a / self.b
#         else:
#             return "Cannot divide by zero"
        
# class Modulos:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
    
#     def modulos(self):
#         if self.b != 0:
#             return self.a % self.b
#         else:
#             return "Cannot modulos by zero"
        
# class Calculator(Division, Modulos):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def calculator_method(self):
#         divval = Division.divide(self)
#         modval = Modulos.modulos(self)
#         return "Division: {}, Modulos: {}".format(divval, modval)
    
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c1 = Calculator(a, b)
# print("Division and Modulos:", c1.calculator_method())
# print("Division:", c1.divide())
# print("Modulos:", c1.modulos())


#3. Multilevel Inheritance
# class Grandparent:
#     def grandparent_method(self):
#         return "This is a method in the Grandparent class"    
# class Parent(Grandparent):
#     def parent_method(self):
#         return "This is a method in the Parent class"
# class Child(Parent):
#     def child_method(self):
#         return "This is a method in the Child class"
# class FutureChild(Child):
#     def future_child_method(self):
#         return "This is a method in the FutureChild class"
    
# c1 = FutureChild()
# print(c1.future_child_method())
# print(c1.child_method())
# print(c1.parent_method())
# print(c1.grandparent_method())
# print("-------------------------------------------------------------------")
# c2 = Child()
# print(c2.child_method())
# print(c2.parent_method())
# print(c2.grandparent_method())

#Galaxy -> Milky Way -> Solar System -> Earth -> Humans -> Future Humans 
#4. Hierarchical Inheritance
# class Parent:
#     def parent_method(self):
#         return "This is a method in the Parent class"
# class Child1(Parent):
#     def child1_method(self):
#         return "This is a method in the Child1 class"
# class Child2(Parent):
#     def child2_method(self):
#         return "This is a method in the Child2 class"
# class Child3(Parent):
#     def child3_method(self):
#         return "This is a method in the Child3 class" 

# c1 = Child1()
# c2 = Child2()
# c3 = Child3()
# print(c1.parent_method())
# print(c1.child1_method())
# print(c2.parent_method())
# print(c2.child2_method())
# print(c3.parent_method())
# print(c3.child3_method())
# print("-------------------------------------------------------------------")
# print(c3.child1_method())

#5. Hybrid Inheritance - A combination of two or more types of inheritance.
# class CEO:
#     def method_ceo(self):
#         return "This is method 1 from CEO"    
# class Manager(CEO):
#     def method_manager(self):
#         return "This is method 2 from Manager"
# class Employee(CEO):
#     def method_employee(self):
#         return "This is method 3 from Employee"    
# class Intern(Employee, Manager):
#     def child_method(self):
#         return "This is a method in the Child class"
    
# i1 = Intern()
# print(i1.child_method())
# print(i1.method_ceo())
# print(i1.method_manager())
# print(i1.method_employee())

#Super() function - Used to call a method from the parent class in the child class. It is used to avoid the ambiguity of method names in multiple inheritance. It will strictly follow the MRO (Method Resolution Order) to call the method from the parent class. It is used to call the method from the parent class in the child class. It is used to avoid the ambiguity of method names in multiple inheritance. It will strictly follow the MRO (Method Resolution Order) to call the method from the parent class. It is used to call the method from the parent class in the child class. It is used to avoid the ambiguity of method names in multiple inheritance. It will strictly follow the MRO (Method Resolution Order) to call the method from the parent class. It is used to call the method from the parent class in the child class. It is used to avoid the ambiguity of method names in multiple inheritance. It will strictly follow the MRO (Method Resolution Order) to call the method from the parent class. It is used to call the method from the parent class in the child class. It is used to avoid the ambiguity of method names in multiple inheritance. It will strictly follow the MRO (Method Resolution Order) to call the method from the parent class. It is used to call the method from the parent class in the child class. It is used to avoid the ambiguity of method names in multiple inheritance. It will strictly follow the MRO (Method Resolution Order) to call the method from the parent class. It is used to call the method from the parent class in the child class. It is used to avoid the ambiguity of method names in multiple inheritance. It will strictly follow the MRO (Method Resolution Order) to call the method from the parent class. It is used to call the method from the parent class in the child class. It is used to avoid the ambiguity of method names in multiple inheritance. It will strictly follow the MRO (Method Resolution Order) to call the method from the parent class. It is used to call the method from the parent class in the child class. It is used to avoid the ambiguity of method names in multiple inheritance. It will strictly follow the MRO (Method Resolution Order) to call the method from the parent class. It is used to call the method from the parent class in the child class.
# class A:
#     def method(self):
#         print("This is method from class A")
#         #super().method()

# class B(A):
#     def method(self):
#         print("This is method from class B")
#         super().method()

# class C(A):
#     def method(self):
#         print("This is method from class C")
#         super().method()

# class D(B, C):
#     def method(self):
#         print("This is method from class D")
#         super().method()

# d1 = D()
# d1.method()