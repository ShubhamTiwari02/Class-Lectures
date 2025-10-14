#Function - a block of code that performs a specific task, can be reused, takes input and returns output
#Function - def(keyword who tells compiler that we are defining a function) function_name(parameters/arguments):

#Functions are of 3 types - built-in functions, user-defined functions, functions from modules
#Built-in functions - print(), input(), len(), type(), int(), str(), float(), sum(), min(), max(), abs(), round()
#User-defined functions - functions defined by the user using def keyword
#Function syntax - def function_name(parameters "self" - must to be provided):

def greet():
    print("Hello, Good morning!")
    li = [1,2,3,4,5,6,7,8,9,10]
    for i in range(len(li)):
        print(f"{li[i]} Have a nice day!")

def printNameFunction(name): #function with parameter/ Parameterized function
    print("Hello " + name + ", Good morning!")

printNameFunction("Yashika") #function call with argument
printNameFunction("Raghav") #function call with argument
printNameFunction("Shubham") #function call with argument
printNameFunction("Kunal") #function call with argument
printNameFunction("Aman") #function call with argument
printNameFunction("Sakshi") #function call with argument
#printNameFunction() #function call without argument - will give error because parameter is mandatory
#printNameFunction("Ankit", "Good evening!") #function call with two arguments - will give error because function is defined with one parameter

#greet() #function call

#The term parameter and argument can be used fro the same thing, information that are passed into a function
#From a function prospective:- 
#Parameter - is a variable listed inside the parentheses in the function definition
#Argument - value that is sent to the function when it is called

#def kids_name(*kids): #Parameterized function with variable number of arguments
#    print("Total number of kids:", len(kids)) #printing total number of arguments
#    print("The youngest child is " + kids[len(kids)-1]) #accessing last element
    #print("End of function") #printing all elements

#kids_name("Shiwani", "Rohan", "Aarav", "Kabir") #function call with four arguments
#kids_name("Kanish", "Rohan", "Kiara") #function call with three arguments
#kids_name("Verma", "Sharma") #function call with one argument
#kids_name("A", "B", "C", "D", "E", "F") #function call without argument - will not give error because parameter is variable number of arguments
#kids_name() #function call without argument - will not give error because parameter is variable number of arguments

#keyword arguments - arguments that are passed to a function by explicitly specifying the parameter name

#def printInfo(name, age): #function with two parameters
#    print("Name:", name)
#    print("Age:", age)

#printInfo(age=25, name="Yashika") #function call with keyword arguments
#printInfo(name="Raghav", age=30) #function call with keyword arguments
#printInfo("Shubham", 28) #function call with positional arguments
#printInfo(32, "Aman") #function call with positional arguments

#Call by value vs Call by reference
#def add(): #function with two parameters
#    a = int(input("Enter first number:")) #taking input from user
#    b = int(input("Enter second number:")) #taking input from user
#    print(a + b) #return statement - returns the value to the caller

#add() #function call with arguments
#Arbitrary arguments - *args (non-keyworded variable length arguments) and **kwargs (keyworded variable length arguments)

def print_lastName(**p_info): #function with variable number of keyword arguments - **kwargs store all arguments in a dictionary
    print("Total last name of the person is :", p_info["lastName"]) #printing total number of arguments

print_lastName(lastName="Sharma", firstName="Yash", age=25, city="New Delhi", country="India", pinCode=110001) #function call with four keyword arguments
print_lastName(firstName="Raghav", age=30, city="Mumbai", lastName="India", pinCode=400001) #function call with three keyword arguments
print_lastName(lastName="Verma", firstName="Shubham") #function call with two keyword arguments
#print_lastName() #function call without argument - will not give error because

def kids_name(**kids): #Parameterized function with variable number of arguments
    print("The youngest child is " + kids["youngest"]) #accessing last element
    #print("End of function") #printing all elements

kids_name(thirdYoungest="Shiwani", secondYoungest="Rohan", youngest="Aarav", fourthYoungest="Kabir") #function call with four arguments
kids_name(youngest="Kanish", secondYoungest="Rohan", thirdYoungest="Kiara") #function call with three arguments
kids_name(youngest="Verma", secondYoungest="Sharma") #function call with one argument
kids_name(fourthYoungest="A", secondYoungest="B", thirdYoungest="C", youngest="D", fifthYoungest="E", sixthYoungest="F")

#Return type - returns a value and exits the function
def add(a, b):
    return a + b 
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def mod(a, b):
    return a % b

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = 10
d = 20
addition = add(a, b)
addition1 = add(c, d)
addition2 = add(100, 200)
print("Addition:", add(a, b))
print("Addition1:", add(c, d))
print("Addition2:", add(100, 200))
print("Subtraction:", sub(a, b))
print("Multiplication:", mul(a, b)) 

def add(x, y):
    pass
def sub(x, y):
    pass
def mul(x, y):
    pass  
def div(x, y):
    pass

x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
add(x, y)
sub(x, y)
mul(x, y)
div(x, y)
print("End of the program", x, y)
#------------------------------------------------------------------------------------------
def my_function(x,y,/): #positional only parameter
    print(x**3)

my_function(10, 5)
my_function(x=10, y=5)
#------------------------------------------------------------------------------------------
def my_function(*, x, y): #keyword only parameter
    print(x**3)
    print(y**3)

my_function(x=10, y=5)
my_function(y=3, x=4)

my_function(10, 5) #TypeError: my_function() takes 0 positional arguments but 2 were given

#call func on a list
#def recur_func(n):
#    if n > 0:
#        result = n + recur_func(n-1)
#        print(result)
#    else:
#        result = 0
#        print(result)
#    return result

#recur_func(5)
#recur_func(3)
#recur_func(10)
#recur_func(15)

#def factorial(n):
#    if n == 0 or n == 1:
#        return 1
#    else:
        #print(n)
#        return n*factorial(n-1)
    

#print(factorial(10))
#print(factorial(5))    
#print(factorial(0))
#print(factorial(1))
#print(factorial(3))
#print(factorial(4))

def main(food):
    for i in food:
        print(i*2)

#main(5)
food = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
food1 = ["carrot", "potato", "cabbage", "onion", "spinach"]
main(["sandwich", "burger", "pizza", "pasta", "salad"])
main(food1)
main(food)

#Scope of variables - local, global and nonlocal
#local variable - defined inside a function and can only be accessed inside that function
#global variable - defined outside a function and can be accessed anywhere in the program
#x = int(input("Enter a number: "))

#def find_even_odd(num):
#    print(f"The number {num} is being checked.")
#    if num % 2 == 0:
#       return "Even"
#    else:
#        return "Odd"

#result = find_even_odd(x)
#print(f"The number {x} is {result}.")

#def my_function():
#    a = 10
#    b = 20
#    print("Inside function:", a, b)
#    return a + b

#print("Outside function:", my_function())
#print("Outside function:", a, b) #will give error because a and b are local variables - NameError: name 'a' is not defined

#Nonlocal variable - defined inside a nested function and can be accessed in the nested function

#x = int(input("Enter a number: "))
#def your_A_and_B():
#    a = 10
#    b = 20
#    def my_A_and_B():
#        nonlocal a, b
#        a = 30
#        b = 40
#        print("Inside inner function:", a+b+x)
#        return a + b + x


#    print("After inner function call:", my_A_and_B())
#print("After outer function call:", your_A_and_B())
#print("Outside function:", a, b) #will give error because a and b are local variablesprint(global()) #will give all global variables
#print(globals()) #will give all global variables


name = "Shivam Kumar"
marks = 90
result = True

def myfunction():
    a = 10
    b = 20
    c = a+b
    print(globals())
    print(locals())
    return c 
    

print(myfunction())

name = "Akash"
marks = 90
result = True

def myfunction():
    a = 10
    b = 20
    c = a+b
    print(globals())
    print(locals())
    print(globals()['name'])
    print(globals().get('marks'))
    print(locals().get('a'))
    print(locals()['b'])
    return c 

print(myfunction())

#Namespace conflict - if variable with same name in local and global, then interpreter gives priority to local Namespace
marks = 50 #this is a global variable
def myfuction():
    marks = 70
    print(marks) #this is a local variable
    
myfuction()
print(marks)

#Manupulation of a global variable inside a function is not allowed when you are not redefining the variable
marks = 50 #this is a global variable
def myfuction():
    #marks = 70
    marks = marks + 20
    print(marks) #this is a local variable
    
myfuction()
print(marks)

#Option 1
#Manupulation of a global variable inside a function is allowed only when you are defining inside a function with keyword "global"
marks = 50 #this is a global variable
def myfuction():
    global marks
    marks = marks + 20
    print(marks) #this is a local variable
    print(globals())
    
myfuction()
print(marks)

#Option 2
#Manupulation of a global variable inside a function is allowed only when you are defining inside a function with keyword "global"
marks = 50 #this is a global variable
def myfuction():
    globals()['marks'] = globals()['marks']+20
    print(marks) #this is a local variable
    #print(globals())
    
myfuction()
print(marks)

#NameError - if variable is defined inside a function and trying to access outside the function
var1 = 30
var2 = 50

def myfunction(var1, var2):
    total = var1+var2
    print("Total is:-", total)
    
myfunction(var1, var2)

print(total)

