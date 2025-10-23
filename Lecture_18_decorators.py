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

print(my_name())  '''

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
