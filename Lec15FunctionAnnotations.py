def my_function(a: int, b: int):
    print(type(a), type(b))
    c = a+b
    return c 
    
print(my_function(10,20))
print(my_function("Hello","world"))

#Function Annotation with return type
def add_numbers(a: 'Enter a number', b: 'Enter another number') -> "":
    return a + b

print(add_numbers(5, 10))  
print(add_numbers("Hello, ", "World!"))
print(add_numbers.__annotations__)