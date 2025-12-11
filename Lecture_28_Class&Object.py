#First concept of OOP: Classes and Objects
class Employee:
    #Constructor to initialize the object
    employee_count = 0  
    def __init__(abc, name, position, salary, age, city, experience):
        abc.name = name
        abc.position = position
        abc.salary = salary
        abc.age = age
        abc.city = city
        abc.experience = experience
        Employee.employee_count += 1

    #Method to display employee details
    def display_info(abc):
        print(f"Name: {abc.name}, Position: {abc.position}, Salary: ${abc.salary}, Age: {abc.age}, City: {abc.city}, Experience: {abc.experience}")

    def display_count():
        print(f"Total Employees: {Employee.employee_count}")


#class object attribute
e1 = Employee("Alice", "Developer", 70000, 30, "New York", 5)
e2 = Employee("Bob", "Designer", 65000, 28, "San Francisco", 4)
e3 = Employee("Charlie", "Manager", 80000, 35, "Chicago", 10)
e4 = Employee("Diana", "Intern", 30000, 22, "Boston", 1)
e5 = Employee("Ethan", "Analyst", 60000, 27, "Seattle", 3)

#delattr(e3, 'position')

#e1.salary = 30  # Dynamically adding attribute to object e1
#e2.position = "Design"  # Dynamically adding attribute to object e2

#del e3.position
#salary = 40  # Local variable, not related to class attribute

#print(e3.salary)  # Accessing attribute of object e4

#e1.display_info()  
#e2.display_info()  
#e3.display_info()  
#e4.display_info()
#e5.display_info()
#Employee.display_count()
#print(type(e1))  
print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__bases__)
print(Employee.__dict__)

# flag_check = hasattr(e1, 'salary')  # Check if e1 has attribute 'salary'
# flag_check_position = hasattr(e3, 'position')  # Check if e3 has attribute 'position'
# print(flag_check)  # Output: True
# print(flag_check_position)  # Output: False
#setattr(e2, 'salary', 70000)  # Set attribute 'salary' of e2 to 70000
#e2.display_info()
#getattr(e3, 'position')  # Get attribute 'position' of e3
#delattr(e4, 'position')  # Delete attribute 'position' of e4
#e5.display_info()

class Sample:
    __hidden_variable = 0  
    def count(self):
        self.__hidden_variable += 1
        return self.__hidden_variable
    
s1 = Sample()
s2 = Sample()
print(s2.count())  # Output: 1
print(s2.count())  # Output: 2
print(s1.count())  # Output: 1
print(s2.count())  # Output: 3
#print(s1._Sample__hidden_variable)
print(s1.__hidden_variable)
print(s1.hidden_variable)

# # class Point:
# #     def __init__(self, x=0, y=0):
# #         self.x = x
# #         self.y = y

# #     def display(self):
# #         print(f"Point({self.x}, {self.y})")

# #     def __del__(self):
# #         class_name = self.__class__.__name__
# #         print(f"{class_name} object is being destroyed")

# # p1 = Point()
# # p2 = p1
# # p3 = p2
# # print(id(p1), id(p2), id(p3))
# # del p1
# # del p2
# # del p3
# # print(id(p1))

# #Data Hiding
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.__account_number = account_number  # Private attribute
#         self.__balance = balance  # Private attribute

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited: ${amount}")
#         else:
#             print("Deposit amount must be positive")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew: ${amount}")
#             print(f"your account number {self.__account_number} has been debited by {amount}")
#             print(f"New balance: ${self.__balance}")
#         else:
#             print("Insufficient funds or invalid withdrawal amount")

#     def get_balance(self):
#         print(f"Balance: ${self.__balance}")
    
# b1 = BankAccount("123456789", 1000)
# #b1.withdraw(200)
# #b1.deposit(500)
# #b1.get_balance()
# print(b1.account_number)  # Accessing private attribute (not recommended)
#----------------------------------------------------------------------------------------------

# class Sample:
#     __hidden_variable = 0  
#     def count(self):
#         self.__hidden_variable += 1
#         return self.__hidden_variable
    
# s1 = Sample()
# s2 = Sample()
# print(s2.count())  # Output: 1
# print(s2.count())  # Output: 2
# print(s1.count())  # Output: 1
# print(s2.count())  # Output: 3
# #print(s1._Sample__hidden_variable)
# print(s1.__hidden_variable)
# print(s1.hidden_variable)

# class Employee:
#     name = "Akash"
#     age = 30

# class Employee1:
#     name = "Raghav"
#     age = 25

# e1 = Employee()
# e2 = Employee1()
# print(e1.name, e2.name)
# print(e1.age, e2.age)

# class Employee:
#     empcount = 5 #Class attributes
#     def __init__(self, name = "Akash", age = 500): #Instance attributes
#         self.name = name
#         self.age = age
#         Employee.empcount += 1
#         print("Name = ", name, ", Age:- ", age)
#         print("Employee count is = ", Employee.empcount)


# e1 = Employee("Shubham", 1090)
# e2 = Employee("Kanak")
# e3 = Employee("Raghav", 24)

#the attributes defined directly inside the __init__() function - Instance attributes
#the attributes defined inside the class but outside the __init__() function - Class attributes

#can be accessed by object name/object only - Instance attributesxccx
#can be accessed by object and class name - class attributes

#value of attributes cannot be shared among the other objects - Instance attributes
#value of attributes can be shared among the other objects - class attributes

#changes made to instance attribute affects only the object within which it is defined - Instance attributes
#changes made to class attrubute affects all the object of the given class - Class attributes

#Methods - functions defined to perform a dedicated activity/operations. Methods are devided into 3 catogories
#1. Class Methods    2. Instance Method - they have access to class and instance attributes
#3. Static Methods

# class Employee:
#     empCount = 0
#     def __init__(self, name = "Akash", age = 30):
#         self.name = name
#         self.age = age
#         Employee.empCount += 1

#     @classmethod
#     def showCount(self):
#         print(self.empCount)

#     @classmethod
#     def newEmployee(self, name, age):
#         print(self(name, age))

#     #counter = classmethod(showCount)

# e1 = Employee("Kunal", 24)
# #e1.showCount()
# e2 = Employee("Raghav", 27)
# e3 = Employee("Shubham", 89)
#e1.showCount()
#Employee.showCount(e1)
#Employee.showCount()
#--------------------------------------------------------------------------------------
# class Employee:
#     empCount = 0
#     def __init__(self, name = "Akash", age = 30):
#         self.name = name
#         self.age = age
#         #self(name, age)
#         Employee.empCount += 1

#     def Employee(self):
#         print("This is Employee function", self.name)

#     @classmethod
#     def showCount(self):
#         print(self.empCount)

#     @classmethod
#     def newEmployee(self, name, age):
#         return self(name, age)

# e1 = Employee("Kunal", 24)
# e2 = Employee("Raghav", 27)
# e3 = Employee("Shubham", 89)
# e4 = Employee.newEmployee("Yashika", 27373277)
# #e1.Employee()
# Employee.showCount()

# class Raghav:
#     money = 400000 #class attribute

#     @classmethod
#     def showMoney(kunal):
#         return kunal.money
    
# print(Raghav.showMoney())