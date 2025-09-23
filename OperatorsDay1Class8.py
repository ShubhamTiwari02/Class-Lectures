#Python operators - arithmetic, comparison, logical, bitwise, assignment, membership, identity
#Operators - 2 types - unary(needs single operand) and binary (needs two or more than two operands)


#Arithmetic operators - +, -, *, /, %, //, **
a = 10
b = 20
c = 0


c = a + b #addition
print("a:{}, b:{}, The total of a and b is:{}".format(a, b, c))
c = a - b #subtraction
print("a:{}, b:{}, The difference of a and b is:{}".format(a, b, c))
c = a * b #multiplication
print("a:{}, b:{}, The product of a and b is:{}".format(a, b, c))
c = a / b #division
print("a:{}, b:{}, The division of a by b is:{}".format(a, b, c))
c = b % a #modulus
print("a:{}, b:{}, The modulus of a and b is:{}".format(a, b, c))
c = b // a #floor division
print("a:{}, b:{}, The floor division of a by b is:{}".format(a, b, c))
d = 2
e = 2
c = d ** e #exponentiation
print("d:{}, e:{}, The exponentiation of d and e is:{}".format(d, e, c))


#Comparison operators - ==, !=, >, <, >=, <=
c = a == b #equal to - it returns a boolean value True or False
print("a:{}, b:{}, The result of a == b is:{}".format(a, b, c))
c = a != b #not equal to
print("a:{}, b:{}, The result of a != b is:{}".format(a, b, c))
c = a > b #greater than
print("a:{}, b:{}, The result of a > b is:{}".format(a, b, c))
c = a < b #less than
print("a:{}, b:{}, The result of a < b is:{}".format(a, b, c))
a = 10
b = 10
c = a >= b #greater than or equal to
print("a:{}, b:{}, The result of a >= b is:{}".format(a, b, c))
c = a <= b #less than or equal to
print("a:{}, b:{}, The result of a <= b is:{}".format(a, b, c))


#Logical operators - and, or, not
var = 5
c = var > 2 and var < 10 #and - returns True if both conditions are True
print("var:{}, The result of var > 2 and var < 10 is:{}".format(var, c))
c1 = var > 2 or var < 4 #or - returns True if at least one condition is True
print("var:{}, The result of var > 2 or var < 4 is:{}".format(var, c1))
c2 = not(var > 2 and var < 10) #not - returns True if the condition is False
print("var:{}, The result of not(var > 2 and var < 10) is:{}".format(var, c2))
print(c, type(c))


#Membership operators - in, not in
my_list = [1, 2.5, "Hello", True, 2, "Raghav"]
a = 2
c = a not in my_list #in - returns True if the value is found in the sequence
print("a:{}, The result of a in my_list is:{}".format(a, c))


#Identity operators - is, is not
a = [1,2,3,4,5]
b = [1,2,3,4,5]
d = 10
e = 10
print(d is e) #True - because both are pointing to the same object in memory
e = 1000
print(d is e) #False - because both are pointing to different objects in memory
c = a
print(a is not b) #is - returns True if both variables point to the same object
print(a is not c)
print(id(a), id(b), id(c))
a = 10
b = a
c = b
d = c
e = 10
f = 20
print(id(a), id(b), id(c), id(d), id(e), id(f))
print(a is b, b is c, c is d, d is e, e is f)
print(a is not b, b is not c, c is not d, d is not e, e is not f)