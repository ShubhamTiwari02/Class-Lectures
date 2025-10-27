#Lambda functions - small anonymous functions defined with the lambda keyword. They can take any number of arguments but can only have one expression.

#z = lambda a: a*1**3
#print(z(500))

#y = lambda a: a+50
#print(y(500))

#x = lambda a, b: a*b
#print(x(500, 100))

#w = lambda a, b, c: a+b+c
#print(w(500, 100, 200))

#Use of lambda function - the power of lambda function is good when you use them as an anonymous function inside another function.

#def sum_function(n):
#    return lambda a: a * n

#result = sum_function(10)
#print(result(20))
#print(sum_function(10)(20))
#print(sum_function(10)(50)) 

#Lambda functions are often used with built-in functions like filter(), map(), sorted() and reduce().
#Filter() - function creates a list of items for which the function returns true.
numbers = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60)
even_numbers = tuple(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

#Map() - function applies a given function to all items in an input list.
squared_numbers = tuple(map(lambda x: x**2, numbers))    
print(squared_numbers)

#Filter() 
odd_numbers = tuple(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#Sorted() - function returns a sorted list of the specified iterable object.
fruits = ['banana', 'apple', 'cherry', 'kiwi', 'mango', 'orange', 'papaya', 'blueberry', 'strawberry', 'fig']
sorted_fruits = sorted(fruits, key=lambda x: len(x))  # Sort by length
print(sorted_fruits)

fruits = ['banana', 'apple', 'cherry', 'kiwi', 'mango', 'orange', 'papaya', 'blueberry', 'strawberry', 'fig']
sorted_fruits = sorted(fruits, key=lambda x: x[-1])  # Sort by last letter
print(sorted_fruits)