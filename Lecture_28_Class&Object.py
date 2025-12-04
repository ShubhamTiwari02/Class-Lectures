#First concept of OOP: Classes and Objects
class Employee:
    #Constructor to initialize the object
    employee_count = 0  
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        Employee.employee_count += 1

    #Method to display employee details
    def display_info(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: ${self.salary}")

    def display_count():
        print(f"Total Employees: {Employee.employee_count}")


#class object attribute
e1 = Employee("Alice", "Developer", 70000)
e2 = Employee("Bob", "Designer", 65000)
e3 = Employee("Charlie", "Manager", 80000)
e4 = Employee("Diana", "Intern", 30000)
e5 = Employee("Ethan", "Analyst", 60000)

print(e4.salary)  # Accessing attribute of object e4

#e1.display_info()  
#e2.display_info()  
#e3.display_info()  
e5.display_info()
Employee.display_count()
#print(type(e1))  # Output: <class '__main__.Employee'>