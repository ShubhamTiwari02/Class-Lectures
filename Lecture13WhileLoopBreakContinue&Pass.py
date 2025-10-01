#while loop - it is used to repeat a block of code as long as a condition is true, and if the
#condition becomes true permanently, the loop will run indefinitely. 

#while Expression: #loop condition/logic - by default it is true
    #statement(s) - block of code
    #code to be executed

#example 1
count = 0
#print(id(count))
#while count < 5: #loop condition - true, entered into the loop
#    print(id(count))
#    print("Count is:", count)
#    count += 1
#print("Loop ended")

#example 2
#n = input("Enter a number:")
#while n.isnumeric() == True: #loop condition
#    print("You entered a valid number:", n)
#    n = input("Enter a number:")

#print("You entered an invalid number:", n)
#print("Loop ended")

#example 3
#var1 = 1 #variable 1
#while var1 == 1: #loop condition - true, entered into the loop
#    num = int(input("Enter a number:")) #variable 2
#    print("You entered:", num)
#    var1 = int(input("Enter 1 to continue and 0 to stop:"))

#print("Loop ended")
#ig - wrong username or password - while loop
#ig - ATM machine - while loop

#example 4 - While else statement
#count = 0
#while count < 5: #loop condition - true, entered into the loop
#    print("Count is:", count)
#    break
#else:
#    print("Loop ended as the condition became false")
#print("Outside the loop | program ended")

#flag = True
#while (flag): print("Given flag is false")
#print("Bbye")

#Break statement - it is used to terminate the loop when a certain condition is met 
#Continue statement - it is used to skip the current iteration of the loop when a certain condition
#Pass statement - it is used to avoid getting errors when a statement is required syntactically but

#looping statement:
#condition check:
#    statement(s)

for i in range(1, 11):
    if i == 7:
        break #terminates the loop
    print(i)
print("Loop ended")
    
for letter in "PythonIsAmazingLanguage":
    if letter == "g":
        break #terminates the loop
    print(letter)
print("Loop ended")

var = 10
while var > 0:
    print("Var is:", var)
    var -= 1 #decrement
    if var == 5:
        break #terminates the loop

print("Loop ended")

#example 2 
li = [45, 23, 67, 32, 89, 90, 12, 49, 78, 56] 
for item in li:
    if item == 90:
        break
    print("Item is:", item)
print("Loop ended")

#---------------------------------------------------------------------------------
user_name = input("Enter your username:")
existing_user = ["Navya0", "Shubham1", "Kunal2", "Yash3", "Rohit4", "Sagar5", "Rajat6", "Ankit7"] #DB Query - list of existing usernames
for checking_User in existing_user:
    if user_name == checking_User:
        print("Username already exists, please try again with a different username")
        break #terminates the loop/session
else:
    print("Username is available | you can proceed with the registration")
#--------------------------------------------------------------------------------------
#Continue statement

for letter in "PythonIsAmazingLanguagewhichisVeryEasyToLearnandUseGreatlyandAlsoVeryPowerful":
    if letter == "A" or letter == "a":
        print("Found an 'A' or 'a', skipping...")
        continue #skips the current iteration
    print(letter, end="-")

#Pass statement
#it is used to avoid getting errors when a statement is required syntactically but you do not want to
#do anything

#for letter in "PythonIsAmazingLanguagewhichisVeryEasyToLearnandUseGreatlyandAlsoVeryPowerful":
for letter in "ABCDEFGHIJKLMNOP":
    if letter == "D" or letter == "M":
        pass #does nothing, avoids error
        print("This is pass block, doing nothing for 'D' or 'M'")
    print(letter)

x = int(input("Enter a number:")) 

if x%2 == 0:
    pass
else:
    print("Its a odd number")

while True:
    print("Hello World")
    pass

#x = int(input("Enter a number:")) 

#if x%2 == 0:
#    ... #ellipses
#else:
#    print("Its a odd number")
