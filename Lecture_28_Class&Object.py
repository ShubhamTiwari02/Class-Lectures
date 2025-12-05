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

