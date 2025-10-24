'''import math
print(math.sqrt(16))
print(math.pi)
print(math.factorial(5))
import random
#print(dir(random))
#random.randint(1,10000)
print(random.randint(1,10000))'''


# Decorators - are a way to modify or enhance functions or methods without changing their actual code.

'''def change_case(arg):
    def inner_func():
        return arg().upper()
    return inner_func

@change_case
def my_name():
    return "hello raGhav, how Are yoU?"

print(my_name())  

def change_Uppercase(arg):
    def inner_func():
        return arg().upper()
    return inner_func

def change_Lowercase(arg):
    def inner_func():
        return arg().lower()
    return inner_func

@change_Uppercase
def my_Uppername():
    return "hello raGhav, how Are yoU?"

@change_Lowercase
def my_Lowername():
    return "hello raGhav, how Are yoU?"

@change_Uppercase
def my_Uppername1():
    return "where there is a will there is a way. this is raGhav speaking wHo loves to coDe."

print(my_Lowername()) 
print(my_Uppername())
print(my_Uppername1())

#Multiple decorators

def greet_decorator(arg):
    def inner_func1():
        #print("Hello", arg())
        return "Hello! " + arg() + " Have a nice day."  
    return inner_func1

def change_Uppercase(arg):
    def inner_func2():
        return arg().upper()
    return inner_func2

@greet_decorator
@change_Uppercase
def my_greeting():
    return "As-salamu alaykum, SHubHAM TIwarI here."


@greet_decorator
def your_greeting():
    return "As-salamu alaykum, SHubHAM TIwarI here."

print(my_greeting()) 
print(your_greeting())

#Decorator with arguments
def changcase(n):
    def change_Uppercase(arg):
        def inner_func():
            if n == 1:
                return arg().upper(),n 
            elif n == 2:
                return arg().lower(),n
            else:
                return arg()
        return inner_func
    return change_Uppercase

@changcase(1)
def my_name():
    return "hello raGhav, how Are yoU?"

print(my_name())

def changcase(func):
    def my_inner(name):
        return func(name.upper())
    return my_inner

@changcase
def my_function(abc, xyz, pqr):
    return f"Hello, {abc}, {xyz}, and {pqr}! how ARE you doing today?"

print(my_function("Raghav", "Shubham", "Anjali")) 
print(my_function("Shubham"))
print(my_function("Anjali"))
print(my_function("Priya"))'''

def changecase(func):
    def my_inner(*args):
        return func(*args).upper()
    return my_inner

@changecase
def my_function(*args):
    return f"Hello, {', '.join(args)}! how ARE you doing today?"
print(my_function("Raghav", "Shubham"))
print(my_function("Anjali", "Priya"))
print(my_function("Sonia", "Monica", "Rachel"))
print(my_function("Chandler", "Joey", "Ross", "Phoebe"))