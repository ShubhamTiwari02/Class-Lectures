# #File operations in Python - we can read, write, and append to files using built-in functions.
# #File handling is an important part of any web application. 
# #File handling is an important part of programming while working with data like retrieving data from a file, writing data to a file, and appending data to a file.
# #modes of file operations
# # 'r' - Read mode which is used when the file is only being read
# # 'w' - Write mode which is used to edit and write new information to the file
# # 'a' - Append mode which is used to add new data to the end of the file; that is new information is automatically amended to the end
# # 'r+' - Special read and write mode, which is used to handle both actions when working with a file
# # 'x' - Create mode which is used to create the specified file, returns an error if the file exists
# #'t' or 'b' - Text or Binary mode which is used to specify the type of file you are working with. Default is text mode
# #f = open("C:\\Users\\ragha\\sample.txt", "r")  # Open a file in read mode
# #f = open("sample.txt", "r")  # Open a file in read mode
# #print(f.read())            # Read the contents of the file
# #f.close()                  # Close the file
# #with open("sample.txt", "r") as f:  # Open a file in read mode
#     #print(f.read())            # Read the contents of the file
#     #print(f.readlines())            # Read the contents of the file
#     #print(f.readline())            # Read the contents of the file
#     #print(f.readline())            # Read the contents of the file
#     #print(f.readline())            # Read the contents of the file
#     #for x in f:
#     #    print(x)

# #----------------- writing a file or appending to a file -----------------
# with open("sample.txt", "w") as file:  # Open a file in write mode
#     file.write("\nThis is the new line added.")  # Write a new line to the file
#     file.write("\nRaghav is not a goodboy at all.")  # Write another new line to the file

# #with open("sample.txt", "r") as f:  # Open a file in read mode
# #    print(f.read())                 # Read the contents of the file

# with open("sample.txt", "a") as file:  # Open a file in append mode
#     file.write("\nThis is the new line added.")  # Write a new line to the file
#     file.write("\nRaghav is not a goodboy at all.")  # Write another new line to the file

# #with open("sample.txt", "r") as f:  # Open a file in read mode
# #    print(f.read())                 # Read the contents of the file

# #----------------- reading or appending a file if it doesn't exist -----------------
# with open("sample1.txt", "w") as file:  # Open a file in write mode
#     file.write("\nThis is the new line added.")  # Write a new line to the file
#     file.write("\nRaghav is not a goodboy at all.")  # Write another new line to the file

# #with open("sample.txt", "r") as f:  # Open a file in read mode
# #    print(f.read())                 # Read the contents of the file

# with open("sample2.txt", "a") as file:  # Open a file in append mode
#     file.write("\nThis is the new line added.")  # Write a new line to the file
#     file.write("\nRaghav is not a goodboy at all.")  # Write another new line to the file

# #with open("sample.txt", "r") as f:  # Open a file in read mode
# #    print(f.read())                 # Read the contents of the file

# #----------------- using 'x' mode to create a file -----------------
# #with open("sample3.txt", "x") as file:  # Open a file in create mode
# #    file.write("\nThis is the new line added.")  # Write a new line to the file
# #    file.write("\nRaghav is not a goodboy at all.")  # Write another new line to the file

# with open("sample2.txt", "r") as file:  # Open a file in append mode
#     file.write("\nThis is the new line added.")  # Write a new line to the file
#     file.write("\nRaghav is not a goodboy at all.")  # Write another new line to the file

# #with open("sample.txt", "r") as f:  # Open a file in read mode
# #    print(f.read())                 # Read the contents of the file

#import os
#os.remove("sample3.txt")  # Delete the file named sample3.txt
# if os.path.exists("sample2.txt"):
#     os.remove("sample2.txt")  # Delete the file named sample2.txt
# else:
#     print("The file does not exist")
#os.rmdir("myfolder")  # Delete the folder named myfolder

