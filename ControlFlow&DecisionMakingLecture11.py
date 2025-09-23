#Control statements/Flow control - if, if-else, if-elif-else, nested if
#Decision making statements
#marks = int(input("Enter your marks: "))
#if marks <= 33:
#    print("You are fail and need to reappear for the exam, Your marks are:", marks)
#else:
#    print("Congratulations! You have passed the exam. Your marks are:", marks)

#if marks < 40:
#    print("you need to work hard")
#print("----------------------------")


'''marks = int(input("Enter your marks: "))
if marks < 33:
    print("You are fail and need to reappear for the exam, Your marks are:", marks)
elif marks >= 33 and marks < 50:
    print("You have passed the exam, but you need to work hard. Your marks are:", marks)
elif marks >= 50 and marks < 75:
    print("You have passed the exam with good marks. Your marks are:", marks)
elif marks >= 75 and marks < 90:
    print("You have passed the exam with very good marks. Your marks are:", marks)
elif marks > 100:
    print("Invalid marks, please enter marks between 0 and 100.")
else:
    print("Congratulations! You have passed the exam with excellent marks. Your marks are:", marks)

print("Dude, you did a great job!")'''


#match case - Python 3.10 and above
'''def checkvowel(char):
    match char:
        case 'a' | 'A':
            return "It's a vowel"
        case 'e' | 'E':
            return "It's a vowel"
        case 'i' | 'I':
            return "It's a vowel"
        case 'o' | 'O':
            return "It's a vowel"
        case 'u' | 'U':
            return "It's a vowel"
        case _:
            return "It's not a vowel"

char = input("Enter a character: ")
print(checkvowel(char))'''


