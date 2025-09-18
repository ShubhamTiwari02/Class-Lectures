a = 10
print(id(a)) #memory address
print(id(10))
del a
a = 20
b = a
c = b
del 20
del a
print(id(b), id(c), id(20))
print(a, type(a))
#variable are of two types - local and global - scope of the variable
a, b, c, d = 10, 20.5 , "Yashika", True
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

#python sequence data types - list - [], tuple - (), range - range()
#list - ordered collection of items enclosed in square brackets, mutable, allows duplicate elements
my_list = [1, 2.5, "Hello", True, 2, "Raghav", 3, 4, 5, 6, 7, 8, 9, 10]
tinylist = [123, "Shubham"]
print(my_list, type(my_list))
print(len(my_list), "second list length", len(tinylist)) # length of list
print(my_list[2]) # first element - index starts from 0 and ends at (len-1)
print(my_list[2:]) # slicing - elements from index 2 to 13
print(my_list[0:14:3])
print(my_list[:4])
print(my_list * 2) # repetition
print(my_list + tinylist) # concatenation
print(my_list)
my_list[0] = "Yashika" # mutable - can change the value of a list
print(my_list)