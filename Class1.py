a = 3.14j # long int is not supported in Python 3
b = 2 + 3.14j
print(type(a))
print(type(b))
print(a + b)
a = -987
b = -21.9
c = -3 + 4j 
d = -0*260
e = 4.56e+2j
print(type(a)) # int
print(type(b)) # float
print(type(c)) # complex
print(type(d)) # int
print(type(e)) # complex

#when ever you are defining a string, len function will give you the length of the string which starts from 1 but 
#when you are accessing the string using index it starts from 0
#python strings - sequence of characters enclosed in single or double quotes
str = "Hello World Yashika" #staring from index 0
print(len(str)) #length of string - (len-1) last index
print(str[18]) # first character
print(str[2:7]) # first character to 6th character slicing - substring (string[start:end]) - print function will go (end-1)
print(str[2:]) # from 2nd index to end, end index is exclusive
print(str[:7]) # from start to 6th index
print(str[-1]) # last character
print(str[-5:-1]) # from 5th last to 2nd last character
print(str*2) # repetition
print(str + " Yashika") # concatenation
str[0] = "h" # strings are immutable - cannot change the value of a string
print(str.upper()) # convert to uppercase
print(str.lower()) # convert to lowercase
print(str)
