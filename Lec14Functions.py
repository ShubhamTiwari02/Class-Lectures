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