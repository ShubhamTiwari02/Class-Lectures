#---------------------- List ------------------------------
#ordered, changable and allow duplicates, and items are indexed
#li = ["Apple", "banana", "pineapple", "guvava", "peach", "cherry", "guvava", "peach", "cherry"]
#s = "this is a goodboy"
#li1 = ["Akash", "Raghav", "Kunal", "Shubham"]
#print(li[5])
#li[0] = "Raghav"
#print(li1)
#tl = list(('apple', "guvava", "peach", "cherry"))
#print(tl)
#print(len(li))
#print(s[-3])
#print(li[2:6])
#print(li[-5:-2])
#li.append("Rajat")
#li.append("Raghav")
#li1.extend(li)
#print(len(li))
#li.insert(2,"Shubham")
#print(li1)
#mylist = list(li)
#mylist1 = li[2:7] #Slice method/operator
#mylist = li.copy()
#mylist.sort()
#print(id(li))
#print(mylist1)
#li.remove("peach")
#li.pop(2)
#del li
#li.clear()
#print("Remove the element successfully")
#li.sort(reverse=True)
#print(li)
#li.reverse()
#print(li)
#li.pop()
#print(li)
#l1 = li.count("cherry")
#print(l1)
#l = li1 + li
#li.extend(li1)
#print(li)

li = ["Apple", "banana", "pineapple", "guvava", "peach", "cherry", "guvava", "peach", "cherry", "Chocolate"]
li1 = ["Akash", "Raghav", "Kunal", "Shubham"]

#list comprehension - a concise way to create lists.
'''lc = []
for x in li:
    if "a" in x:
        lc.append(x)

print(lc)'''
lc = [x for x in li if "c" in x] #lambda function - it will add element only the function returns true
print(lc)

lc1 = [x for x in li if x != "peach"]
print(lc1)

#li = ["Apple", "banana", "pineapple", "guvava", "peach", "cherry", "guvava", "peach", "cherry", "Chocolate"]
#li1 = ["Akash", "Raghav", "Kunal", "Shubham"]

#lc = [x*5 for x in range(100) if x % 2 == 0 and x % 3 == 0]
#print(lc)
#lc = [x.upper() for x in li]
#print(lc)
#lc = ['Raghav eats ' + x for x in li]
#print(lc)
s=" eko rakhi jaat ne pyar rakhi phona cho baade ethe fiir de vepaar lage onaa choo"

for i in s:
    if i not in "aeiou":
        print(i,end="")

lc = [char for char in s if char not in "aeiouAEIOU" if char != " " and char != "," and char != "."]
print(lc)

#Tuples
a = (1, 2, 3, 4, 6, 7, 8, 9, 10, 6, 7, 8, 9, 10, 2 ,2 ,3 ,4 ,5, 30, 0)
b = ("Apple", "Banana", "Cherry", "Mango")
#a.append(6)  # This will raise an AttributeError since tuples are immutable
#a[2] = 10  # This will raise a TypeError since tuples do not support item assignment
#a.pop()  # This will raise an AttributeError since tuples do not have a pop method
#------- you have to change a value in a tuple by converting it to a list and back to a tuple -------
#temp = list(a)
#temp.pop(0)
#temp.remove(1)
#temp.pop()
#temp.append("Apple")
#temp.append(7)
#temp[5] = 10
#a = tuple(temp)
#del a # deleting the entire tuple
#c = a + b # concatenation - Adds two tuples and creates a new tuple
#print(c)
#print(type(c))
#z = a.count(30)  # counts the number of occurrences of a value
#z1 = a.index(5)  # returns the index of the first occurrence of a value
#x = max(a)  # returns the maximum value
#y = min(a)  # returns the minimum value
#z = len(a)  # returns the length of the tuple
#f = sum(a)  # returns the sum of all elements in the tuple
#print(x, y, z, f)
