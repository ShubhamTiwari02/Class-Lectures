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

#------------------------------------------------------------------------------------------------
#Loop for tuple
#sum_tuple = (5, 26, 32, 44, 58, 43, 78, 90, 11, 23, 40, 50)
#sum_t = tuple(int(i) for i in input("Enter numbers separated by space: ").split()) #lambda function
#print(sum_t)
#total = 0
#for i in sum_tuple:
    #print(i, total, sep="->")
#    total = total + i #5----------------------------------
    #print(i, total, sep="->")

#print("Sum of all elements in tuple:", total)

#li = [5, 26, 32, 44, 58, 43, 78, 90, 11, 23]
#for i in li:
#    if i%2 == 0:
#        print(i, "is even")
#    else:
#        print(i, "is odd")

#for i in range(10): #single argument - it takes it as stop, start = 0, step = 1
#    print(i)

#for i in range(10,20):
#    print(i)

#for i in range(0,2,-1):
#    print("Hello")

#print("Program ends here")

#for i in range(1, 10, 2): #single argument - stop, start - 0, step - 1
#    print(i) #1 to 9

#for i in range(11, 21, 2): #single argument - stop, start - 0, step - 1
#    print(i) #1 to 9

#numbers = {10:"Ten", 20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty"}
#a = numbers.items()
#numbers.get(10) #accessing value using key
#for i in numbers.values():
#    print(i)
#even_li = []
#odd_li = []
#for i in range(1, 101): #1 to 100
#    if i % 2 == 0:
#        even_li.append(i)
#    else:
#        #print(i, "is odd")
#        odd_li.append(i)

#print("Even numbers are:", even_li)
#print("Odd numbers are:", odd_li)
#num = int(input("Enter a number to check prime or not: ")) #48371
#for num in range(1, 101): #10
#for i in range(2, num):  #50,000
#    if (num % i) == 0:
#        print(f"{num} % {i} = {num % i}")
#        print(num, "is not a prime number")
#        break  
#else:
#    print(num, "is a prime number")

#range(start, stop, step)
#------------------------------------------------------------------------------------------------
#for else loop
#if i has a factor greater than sqrt(i), the other factor must be less than sqrt(i)
#So, we only need to check for factors from 2 to sqrt(i)


#is_prime = True

#i = int(input("Enter a number to check prime or not: ")) 
#z = int(i**0.5)
#for y in range(2, z+1): #checking divisibility from 2 to sqrt(x), y will be iterate from 2 to sqrt(x)
#    if i % y == 0: #if the nuber is divisible by any number other than 1 and itself
#        is_prime = False
#        break
#if is_prime:
#    print(i, "is a prime number")
#else:
#    print(i, "is not a prime number")
#num = input("Enter a number to write table: ")
#for i in range(1, 11):
    #print(f"{num}*{i} = {num*i}")
#    print(f"{num*i}")
#else:
#    print("Table is completed here, now in else block")
#print("Program ends here | End of for-else loop")

li = [5, 26, 32, 44, 58, 43, 78, 90, 11, 23]
for i in li:
    print(i)
    break
else:
    print("This is else block")

print("Program ends here")