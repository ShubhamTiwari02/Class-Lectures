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
lc = [x for x in li if "c" in x] #lambda function
print(lc)

lc1 = [x for x in li if x != "peach"]
print(lc1)

