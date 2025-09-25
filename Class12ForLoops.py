#Loops - for, while, for else, nested loops, break, continue, pass

# 1. For loop - syntax - string, list, tuple, set, dictionary
# for iterating_var in sequence:
#     statements(s) 
#Repeatition structure - for loop and while loop 
#s = [5, 26, 32, 44, 58, 43, 78, 90, 11, 23]
#for i in range(len(s)): #start - 0, stop = 5, step
    #print(i)
#    print(i,s[i], sep =" -> ") #0 -> 5

#s = "This is a thirsty crow, looking for a drop of water and it is very hot day"
#s1 = str(100) 
#print(type(s1))
#print(s1[16])
#for i in s:
#    print(i, end="")
#    print(i[5])

s = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
'''

#for i in s:
#    if i not in "aeiouAEIOU": #If it returns True, it will print the consonants
#        print(i, end="")

#-----------------------------------------------------------------------------------------------
#Loop for tuple
#sum_tuple = (5, 26, 32, 44, 58, 43, 78, 90, 11, 23)
#total = 0
#for i in sum_tuple:
#    print(i, total, sep="->")
#    total = total + i #5----------------------------------
    #print(i, total, sep="->")

#print("Sum of all elements in tuple:", total)

#li = [5, 26, 32, 44, 58, 43, 78, 90, 11, 23]
#for i in li:
#    if i%2 == 0:
#        print(i, "is even")
#    else:
#        print(i, "is odd")

#for i in range(10):
#    print(i)

#for i in range(10,20):
#    print(i)

#for i in range(0,2,-1):
#    print("Hello")

#print("Program ends here")