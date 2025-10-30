li = []
def f_series(n):
    li.append(n)
    if n <= 1:
        return n
    else:
        #li.append(n)
        return f_series(n-1) + f_series(n-2)

print(f_series(10))
print(li)
print(sum(li))
#-------------------------------------------------------------------------------------------
#import sys
#sys.setrecursionlimit(10**6)
#print(sys.getrecursionlimit())
#-------------------------------------------------------------------------------------------
def recur_func(n):
    if n > 0:
        result = n + recur_func(n-1)
        print(result)
    else:
        result = 0
        print(result)
    return result

recur_func(500000)
#recur_func(3)
#----------------------------- Generators --------------------------------------------------------------
#Generators - functions that return an iterable set of items, one at a time, in a special way. They generate values on the fly and do not store them in memory, making them more memory efficient for
#large datasets compared to lists.

#li = [1,2,3,4,5,6,7]
#for value in li:
#    print(value)

def my_func():
    print("Start")
    return [1,2,3,4,5,6,7]

def my_generator():
    yield 1,13,14,15,16
    yield 2
    yield 3
    yield 4
    yield 5

gen = my_generator()

#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))
print(my_func())
print(my_generator())
#print(next(gen)) #------------- This will raise StopIteration error
#print(my_func())
#print(my_generator())
#print(id(50))
#gen = my_generator()
#print(gen[3])
#--------------------------------- Huge Range Generator ------------------------------------------
def huge_range(n):
    for i in range(n):
        yield i

gen = huge_range(10000000)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
#for value in gen:
#    print(value)
#-------------------------- Fibonacci Generator -----------------------------------------------
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator()
for _ in range(20):
    print(next(fib_gen))
#-------------------------------------------------------------------------------------------